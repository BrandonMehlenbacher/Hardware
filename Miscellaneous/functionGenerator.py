import pyvisa as visa

class GeneralSCPI:
    """
    This will be a general class consisting of commands ubiquitously used across SCPI commands
    This will be the parent class for the rest of SCPI hardware components that we will be using in the lab

    Inputs:
    instrument: an opened resource using the visa module
    source: which source on the function generator are you trying to use, a string containing SOUR1

    """
    def __init__(self,instrument,source):
        self.instrument  = instrument
        self.source = source
    def write_single(self,command):
        """
        Input:
        command: a string containing the command you want to write to the instrument
        """
        self.instrument.write(f":{self.source}:{command}")
    def write_many(self,commands):
        """
        Input:
        commands: a list of strings containing the commands you want to write to the instrument
        """
        for command in commands:
            self.write_single(command)

class FunctionGenerator(GeneralSCPI):
    """
    This is going to be used for controlling different components of a function generator attempting to make
    it a little bit cleaner

    For this to work correctly, you will should not do any of the formatting for the commands
    example: :SOUR1:VOLT 6;...
    this should be entered as VOLT 6

    Inputs:
    instrument: an opened resource using the visa module
    source: which source on the function generator are you trying to use, a string containing SOUR1

    """
    def __init__(self, instrument, source):
        super().__init__(instrument,source)
    def change_shape(self,shape):
        """
        Input:
        Voltage: the desired voltage as governed the declared units
        """
        self.write_single(f"FUNC:SHAP "+shape)
    def change_voltage(self,voltage):
        """
        Input:
        Voltage: the desired voltage as governed the declared units
        """
        self.write_single(f"VOLT {voltage}")

class SineWaveform(FunctionGenerator):
    pass
class SquareWaveform(FunctionGenerator):
    pass
class PulseWaveform(FunctionGenerator):
    pass
class DCWaveform(FunctionGenerator):
    pass
class NoiseWaveform(FunctionGenerator):
    pass

if __name__ == "__main__":
    rm = visa.ResourceManager()
    resource = rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD212800749::INSTR',timeout=1)
    instrument = FunctionGenerator(resource,'SOUR1')
    instrument.write_many(["FUNC:SHAP RAMP","VOLT:UNIT VPP","FREQ 10","VOLT 1","FUNC:RAMP:SYMM 50","OUTP ON"])
    #resource.close_resource()
    #instrument.write_single("OUTP ON")
    
