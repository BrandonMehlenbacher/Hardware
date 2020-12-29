import pyvisa as visa
import numpy as np


#rm = visa.ResourceManager()
class oscilloscope:
    def __init__(self,identifier,channel):
        rm = visa.ResourceManager()
        self.oscilloscope = rm.open_resource(identifier)
        self.oscilloscope.query_values("CH4")
        



if __name__ == "__main__":
    resource = oscilloscope('USB0::0x0699::0x03A6::C044574::INSTR','CH4')
