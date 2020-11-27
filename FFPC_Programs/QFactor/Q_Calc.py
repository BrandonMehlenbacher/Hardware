import matplotlib.pyplot as plt
from lmfit.models import LorentzianModel


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
