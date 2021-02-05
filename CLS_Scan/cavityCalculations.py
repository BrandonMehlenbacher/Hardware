import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from lmfit.models import LorentzianModel
from scipy.signal import find_peaks
import numpy as np

def whiteLightScan(data=None, filename = None,toPlot = False):
    if data == None and filename == None:
        print("we do need some data")
        return
    elif data != None:
        wlsData = data
    else:
        wlsData = pd.read_csv(filename,sep=' ', header=None)
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
def fittingCavityLength(data=None,filename = None):
    if data == None and filename == None:
        print("we do need some data")
        return
    elif data != None:
        cls_data = data
    else:
        cls_data = pd.read_csv(filename,header= None)
    resonance = cls_data[2][:5000] # the intensity data
    length = np.arange(len(resonance)) # the length in arbitrary units
    
    resonance = (resonance-np.mean(resonance))
    resonance = resonance/np.max(resonance)
    
    lorenz_1st = LorentzianModel(prefix='L_1')
    lorenz_2nd = LorentzianModel(prefix='L_2')
    lorenz_3rd = LorentzianModel(prefix='L_3')

    x = np.array(length)
    y = np.array(resonance)
    
    list_peaks = find_peaks(y,height = .6, distance = 30)[0]
    if len(list_peaks) != 3:
        linewidth = 0
    else:
        first, second, third = list_peaks
    #print()
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

            L_1sigma = out.best_values['L_1sigma']*2
            L_1center = out.best_values['L_1center']
            L_2center = out.best_values['L_2center']
            linewidth = L_1sigma*2.8993*1000/(abs(L_1center-L_2center))
            return linewidth
            """
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
            linewidth_list.append(linewidth)
            print(first-second)
            print(second-third)
            """
