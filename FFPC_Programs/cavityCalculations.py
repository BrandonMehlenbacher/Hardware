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
            
def efficiency(mode_radius,core_radius,radius_of_curvature,wavelength):
    """
    Inputs:
    mode_radius: radius of the cavity mode inside of the cavity assumed to be in microns
    core_radius: simple def, core of the field, complicated def, mode field radius of the field (extends slightly past core of fiber) assumed to be in microns
    radius_of_curvature: radius of curvature of the fiber, we are assuming a symmetric cavity ie both ROCs are the same. assumed to be in microns
    wavelength: wavelenght of light we plan to optimally use. Assumed to be in microns
    Outputs:
    efficiency: The output is the efficiency of coupling light into the fiber
    """
    #return ((2*mode_radius*core_radius)/(mode_radius**2+core_radius**2))**2
    return 4/(((mode_radius/core_radius)+(core_radius/mode_radius))**2+((np.pi*1.54*mode_radius*core_radius)/(wavelength*radius_of_curvature)))
def mode_radius_fn(radius_curvature,length_cavity,wavelength):
    """
    Inputs:
    radius_curvature: The radius of curvature of the mirror, this function assumes microns
    length_cavity: The length of the cavity, this function assumes length is in microns
    
    Outputs:
    mode_radius: The smallest the spot size gets within the cavity
    """
    return ((wavelength/(2*np.pi))**0.5)*(length_cavity*(2*radius_of_curvature-length_cavity))**0.25

def rayleigh_range(mode_radius_value, wavelength):
    """
    Inputs:
    spot_size: Smallest size inside of the cavity, assumed to be in microns
    wavelength: wavelength of light that will be used, assumed to be in microns
    Outputs:
    rayleigh_range: The rayleigh range if the system in microns
    """
    return (np.pi*mode_radius_value**2)/(wavelength)

def mode_radius_mirror_fn(cavity_length,mode_radius_value,wavelength):
    """
    Inputs:
    cavity_length: length of the cavity in microns
    mode_radius: the minimum mode waist inside of the cavity in microns
    wavelength: wavelength of interest in microns
    Outputs:
    mode_radius on the the cavity mirror
    """
    cavity_length = cavity_length/2
    rayleigh_range_value = rayleigh_range(mode_radius_value,wavelength)
    return mode_radius_value*(1+(cavity_length/rayleigh_range_value)**2)**0.5

def clipping_losses(radius_mirror,mode_radius_value):
    """
    Inputs:
    radius_mirror: radius of the mirror, this is half the diameter of the mirror if you go back to the old fiber spreadsheets, in microns
    mode_radius_value: the size of the mode when it reaches the mirror, calculated from previous mode_radius_mirror, in microns
    Outputs:
    Clipping losses associate wtih the mirror
    """
    return np.exp(-2*((radius_mirror)**2)/(mode_radius_value**2))
def finesse_calculations(cavity_length,mirror_diameter,mode_radius_value):
    """
    Inputs:
    cavity_length: the length of the cavity in microns
    mirror_diameter: the diameter of the mirror in microns
    mode_radius_value: the size of the mode when it reaches the mirror, calculated from previous mode_radius_mirror, in microns
    Outputs:
    Finesse: Calculates the finesse of the cavity in terms of losses
    """
    clipping_loss = clipping_losses(mirror_diameter,mode_radius_value)*2
    finesse_initial = 30000
    total_losses = (2*np.pi)/finesse_initial
    #total_losses = 180*10**-6 # tbh i was lazy and decided a constant starting finesse value, this includes absorption,scattering, and transmission losses
    return (2*np.pi)/(clipping_loss+total_losses)

def cross_sectional_area(mode_radius):
    return np.pi*mode_radius

def diffraction_limited_spot(radius_of_curvature,mirror_diameter,wavelength):
    return (wavelength*radius_of_curvature)/(np.pi*mirror_diameter)
wavevector = lambda x: (2*np.pi)/(x) #x is wavelength and is assumed to be in microns
def cooperativity(finesse,wavevector,spot_size):
    return (24*finesse)/(np.pi*(wavevector**2)*spot_size**2)