import pyvisa as visa

class GeneralSCPI:
    """
    This will be a general class consisting of commands ubiquitously used across SCPI commands
    This will be the parent class for the rest of SCPI hardware components that we will be using in the lab

    Inputs:
    instrument: an opened resource using the visa module
    source: which source on the function generator are you trying to use, a string containing SOUR1

    """
    def __init__(self,instrument,source="SOUR1"):
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
    def query_single(self,command):
        self.instrument.query(f":{self.source}:{command}")
    def get_ID(self):
        self.query_single(f":*IDN?")
    def operation_finished(self):
        self.query_single(f":*OPC")
    def default_state(self):
        self.query_single(f":*RST")
    def wait_finished(self):
        self.query_single(f":*WAI")

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
    def __init__(self, instrument, source="SOUR1"):
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
        assert isinstance(voltage, (int,float))
        if isinstance(self,DCWaveform):
            print("You should be using change_offset instead")
        else:
            self.write_single(f"VOLT {voltage}")
    def change_frequency(self,frequency):
        """
        Input:
        Frequency: the desired voltage as governed the declared units Frequency
        """
        assert isinstance(frequency, (int,float))
        self.write_single(f"FREQ {frequency}")
    def change_offset(self,offset):
        """
        Input:
        Offset: the desired voltage as governed the declared units offset
        """
        assert isinstance(offset, (int,float))
        self.write_single(f"VOLT:OFF {offset}") 

class SineWaveform(FunctionGenerator):
    def __init__(self,instrument,source="SOUR1"):
        super().__init__(self,instrument,source)
        self.change_shape("SINE")
    def change_frequency(self,frequency):
       assert frequency >= 0.1 and frequency <= 25*10**6
       super().change_frequency(frequency)
        
class SquareWaveform(FunctionGenerator):
    def __init__(self,instrument,source="SOUR1"):
        super().__init__(self,instrument,source)
        self.change_shape("SQUA")
    def change_frequency(self,frequency):
       assert frequency >= 0.1 and frequency <= 25*10**6
       super().change_frequency(frequency)
       
class RampWaveform(FunctionGenerator):
    def __init__(self,instrument,source="SOUR1"):
        super().__init__(self,instrument,source)
        self.change_shape("RAMP")
    def change_frequency(self,frequency):
       assert frequency >= 0.1 and frequency <= 25*10**6
       super().change_frequency(frequency)
    def change_symmetry(self,symmetry):
        assert symmetry > 0 and symmetry <= 100
        self.write_single(f"FUNC:RAMP:SYMM {symmetry}")
       
class PulseWaveform(FunctionGenerator):
    def __init__(self,instrument,source="SOUR1"):
        super().__init__(self,instrument,source)
        self.change_shape("PULS")
    def change_frequency(self,frequency):
       assert frequency >= 0.1 and frequency <= 25*10**6
       super().change_frequency(frequency)
       
class DCWaveform(FunctionGenerator):
    def __init__(self,instrument,source="SOUR1"):
        super().__init__(self,instrument,source)
        self.change_shape("DC")
    def change_frequency(self,frequency):
       assert frequency >= 0.1 and frequency <= 25*10**6
       super().change_frequency(frequency)
       
class NoiseWaveform(FunctionGenerator):
    def __init__(self,instrument,source="SOUR1"):
        super().__init__(self,instrument,source)
        self.change_shape("NOIS")
    def change_frequency(self,frequency):
       assert frequency >= 0.1 and frequency <= 25*10**6
       super().change_frequency(frequency)

if __name__ == "__main__":
    rm = visa.ResourceManager()
    resource = rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD212800749::INSTR',timeout=1)
    instrument = FunctionGenerator(resource,'SOUR1')
    instrument.write_many(["FUNC:SHAP RAMP","VOLT:UNIT VPP","FREQ 10","VOLT 1","FUNC:RAMP:SYMM 50","OUTP ON"])
    #resource.close_resource()
    #instrument.write_single("OUTP ON")
    
