import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from lmfit.models import LorentzianModel
from scipy.signal import find_peaks
import numpy as np

def check_data_file(data=None,filename=None,sep = ','):
    """
    This function takes either data as an input or a file that we need to read the data from as the input and send back the data aftewards

    Inputs:
    data: data that is gathered during acquisition
    filename: a filename where we can get the data we want to find the free spectral range, currently assumes a space separated file not comma separated

    Output:
    usedData: Data that we want to further process
    """
    if data == None and filename == None:
        print("we do need some data")
        return
    elif data != None:
        usedData = data
    else:
        usedData = pd.read_csv(filename,sep=sep, header=None)
    return usedData

def whiteLightScan(data=None, filename = None,toPlot = False):
    """
    This function takes either data as an input or a file that we need to read the data from as the input and finds the Free spectral range for our cavities

    Inputs:
    data: data that is gathered during acquisition
    filename: a filename where we can get the data we want to find the free spectral range, currently assumes a space separated file not comma separated
    toPlot: determines if we want to plot our data to see it or not

    Outputs:
    Prints the Free spectral range between the top three peaks in the FSR
    """
    wlsData = check_data_file(data,filename,sep = ' ')
    wlsData[2] = (wlsData[2]-min(wlsData[2]))
    wlsData[2] = wlsData[2]/max(wlsData[2])

    if toPlot:
        plt.plot(wlsData[1][0:1101],wlsData[2][0:1101],color='k')
        plt.xlabel('Wavelength (nm)',fontsize = 16)
        plt.ylabel('Normalized Transmission', fontsize = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
        plt.tight_layout()
        plt.savefig('WLS.png')
    listPeaksWls = find_peaks(data[2],height = .6, distance = 30)[0]
    print(abs(wlsData[1][listPeaksWls[0]]-wlsData[1][listPeaksWls[1]]))
    print(abs(wlsData[1][listPeaksWls[1]]-wlsData[1][listPeaksWls[2]]))
    print(abs(wlsData[1][listPeaksWls[2]]-wlsData[1][listPeaksWls[3]]))
def fittingCavityLength(data=None,filename = None,toPlot = False):
    """
    This function takes either data as an input or a file that we need to read the data from as the input and finds the linewidth  for our cavities

    Inputs:
    data: data that is gathered during acquisition
    filename: a filename where we can get the data we want to find the free spectral range, currently assumes a space separated file not comma separated
    toPlot: determines if we want to plot our data to see it or not

    Outputs:
    Prints the Free spectral range between the top three peaks in the FSR
    """
    clsData = check_data_file(data,filename)
    resonance =  clsData[2][:5000] # the intensity data
    length = np.arange(len(resonance)) # the length in arbitrary units

    # normalize the distribution so that fitting a lorenztian is easier
    resonance = (resonance-np.mean(resonance))
    resonance = resonance/np.max(resonance)
    
    lorenz_1st   = LorentzianModel(prefix='L_1')
    lorenz_2nd  = LorentzianModel(prefix='L_2')
    lorenz_3rd  = LorentzianModel(prefix='L_3')

    x = np.array(length)
    y = np.array(resonance)

    # this entire block of code works based off of generating sidebands for our set-ups
    # phase modulation generates two sidebands separated by a known distance based off of a VCO sent to a phase modulator
    # since this distance is known we can calculate the linewidth based off of this fact since we will have two reference peaks
    # what you see below is just that, it looks for three peaks, fits them, then uses a peaks FWHM to calculate the linewidth
    list_peaks = find_peaks(y,height = .6, distance = 30)[0]
    if len(list_peaks) != 3:
        linewidth = 0
    else:
        first, second, third = list_peaks
        
        if abs(first-second)< 150 and abs(second-third) < 150:
            mid_peak = x[np.argmax(y)]

            #pars = lorenz_1st.guess(y, x=x)
            pars = lorenz_1st.make_params()

            pars['L_1center'].set(value=first, min=first-2,max=first+2)
            pars['L_1sigma'].set(value=1, min=.5)
            pars['L_1amplitude'].set(value=4, min=3)

            pars.update(lorenz_2nd.make_params())

            pars['L_2center'].set(value=second, min=second-2,max=second+2)
            pars['L_2sigma'].set(value=1, min=.5)
            pars['L_2amplitude'].set(value=4, min=3)

            pars.update(lorenz_3rd.make_params())

            pars['L_3center'].set(value=third, min=third-2, max=third+2)
            pars['L_3sigma'].set(value=1, min=.5)
            pars['L_3amplitude'].set(value=4, min=3)

            mod = lorenz_1st + lorenz_2nd + lorenz_3rd

            init = mod.eval(pars, x=x)
            out = mod.fit(y, pars, x=x)

            L_1sigma = out.best_values['L_1sigma']*2 # we want the FWHM so we multiply by 2
            L_1center = out.best_values['L_1center']
            L_2center = out.best_values['L_2center']
            linewidth = L_1sigma*2.8993*1000/(abs(L_1center-L_2center)) # consider changing this to the frequency of VCO
            if toPlot:
                fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8))
                axes[0].plot(x, y, 'b')
                axes[0].plot(x, init, 'k--', label='initial fit')
                axes[0].plot(x, out.best_fit, 'r-', label='best fit')
                axes[0].legend(loc='best')
            
                comps = out.eval_components(x=x)
                axes[1].plot(x, y, 'b')
                axes[1].plot(x, comps['L_1'], 'g--', label='Lorentzian 1st')
                axes[1].plot(x, comps['L_2'], 'm--', label='Lorentzian 2nd')
                axes[1].plot(x, comps['L_3'], 'k--', label='Lorentzian 3rd')
                axes[1].legend(loc='best')
                plt.show()
                #linewidth_list.append(linewidth)
                print(first-second)
                print(second-third)
                
            return linewidth


class QFactor(object):
    """
    Code for calculating the QFactor for our resonators
    Uses the lmfit lorentzian model for doing the fitting

    Inputs:
    x_values: the x_values to be used for plotting
    y_values: signal coming from the APD
    guessesLor: Guesses to be used when fitting the lorentzian
    guessesMod: this will be implemented later and will use
                the modified lorentzian function for fitting parameters
    """

    def __init__(self, x_values, y_values,
                 guessesLor=[1, 1], guessesMod=[0, 0, 0, 0]):
        self._x_values = x_values
        self._y_values = y_values
        self._out = None
        self._center = None
        self._amplitude = guessesLor[0]
        self._sigma = guessesLor[1]
        # self._a = guessesMod[0]
        # self._b = guessesMod[1]
        # self._c = guessesMod[2]
        # self._d = guessesMod[3]
        # will be implemented later currently does not work
    # def fitModLorentz(self):
        # params = curve_fit(self.modLorent,xdata=self._x_values,
        # ydata=self._y_values)
        # return params[0]

    def modLorent(self, a, b, c, d, x):
        return a+(b/(1+((x-c)/d)**2))

    def fitLorentz(self):
        # finds max value to center the peak
        max_arg = self._y_values.index(max(self._y_values))
        mod = LorentzianModel(prefix="L_1")
        pars = mod.make_params()
        pars['L_1center'].set(value=self._x_values[max_arg],
                              min=self._x_values[max_arg]-10,
                              max=self._x_values[max_arg]+10)
        pars['L_1sigma'].set(value=self._sigma, min=0.001)
        pars['L_1amplitude'].set(value=self._amplitude, min=0.001)
        self._out = mod.fit(self._y_values, pars, x=self._x_values)

    def getCenter(self):
        return self._out.best_values['L_1center']

    def getSigma(self):
        return self._out.best_values['L_1sigma']

    def getAmplitude(self):
        return self._out.best_values['L_1amplitude']

    #def getNewYVal(self):
    #    return self._out.eval_components(x=self._x_values)['L_1']

    def get_plot(self):
        newYValues = self._out.best_fit
        plt.plot(self._x_values, self._y_values)
        plt.plot(self._x_values, newYValues, 'k--')
        plt.title("Resonance for Q-Factor")
        plt.ylabel("Relative Intensity")
        plt.xlabel("Relative Wavelength (pm)")
        plt.show()
