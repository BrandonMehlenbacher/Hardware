import pyvisa as visa
import numpy as np
import sys
from functionGenerator import GeneralSCPI

#rm = visa.ResourceManager()
class Oscilloscope(GeneralSCPI):
    """
    This is a class to be used as a oscillscope and was designed using Tektronix oscilloscope

    Inputs:
    instrument: This is after the instrument has been opened using visa
    source: the channel that you are reading from


    """
    
    def __init__(self,instrument,source = "CH1"):
        super().__init__(instrument,source)
    def change_range(self,scale):
        """
        This is a function that changes the vertical voltage range.

        Inputs:
        scale: Desired voltage range as str or int
        """
        try:
            assert isinstance(scale, (int,float))
            self.write_single(f"SCAL {scale}")
        except AssertionError:
            print("Input needs to be a float or integer not a "+str(type(scale)))
            sys.exit()
        
    def change_vertical_position(self, vpos):
         """
        This is a function that changes the vertical position.

        Inputs:
        vpos: Desired vertical position as str or int
        """
         assert isinstance(vpos, (int,float))
         self.write_single(f"POS {vpos}")
        
        
    def change_vertical_offset(self, offs):
        """
        This is a function that changes the vertical offset.

        Inputs:
        offs: Desired vertical offset as str or int
        """
        assert isinstance(offs, (int,float))
        self.write_single(f"OFFS {offs}")
         
        
        
        
        



if __name__ == "__main__":
    rm = visa.ResourceManager()
    instrument = rm.open_resource('USB0::0x0699::0x03A6::C044574::INSTR')
    instrumentClass = Oscilloscope(instrument,"CH4")
    instrumentClass.change_range(2)
   # instrumentClass.change_vertical_position(0)
    instrumentClass.change_vertical_offset(1)
    
