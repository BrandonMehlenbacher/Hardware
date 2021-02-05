from ThorlabsPM100 import ThorlabsPM100, USBTMC
import numpy as np
import win32com.client


class PowerMeter(object):
    def __init__(self,USB_Port,intitial_wavelength=780):
        instr = USBTMC(device=USB_Port) 
        self._power_meter = ThorlabsPM100(inst=instr)
        self._current_wavelength = self.wavelength(initial_wavelength)
    def read(self):
        return self._power_meter.read
    @property
    def wavelength(self):
        return self._current_wavelength
    def wavelength(self,new_wavelength):
        self._power_meter.sense.correction.wavelength(new_wavelength)
        return self._power_meter.sense.correction.wavelength
