import nidaqmx
import numpy as np
from scipy import signal
from nidaqmx import *
import time
"""
test_Task = nidaqmx.Task()
test_Task.ao_channels.add_ao_voltage_chan('Dev1/ao0')
frequency = 100
rate = 1000000
test_Task.timing.cfg_samp_clk_timing(rate=rate,sample_mode= nidaqmx.constants.AcquisitionType.CONTINUOUS)
test_Writer = nidaqmx.stream_writers.AnalogSingleChannelWriter(test_Task.out_stream, auto_start=False)
timePoints = np.linspace(0,1/frequency,int(rate/frequency))
samples = signal.sawtooth(2*np.pi*frequency*timePoints,width = 0.5)
test_Writer.write_many_sample(samples)
test_Task.wait_until_done(timeout=100)
"""

class outputSignal:
    def __init__(self,channel,rate,frequency,continuous = True,signalType=0):
        self.rate = rate
        self.outputTask = nidaqmx.Task()
        self.outputTask.ao_channels.add_ao_voltage_chan(channel)
        self.outputTask.timing.cfg_samp_clk_timing(rate=self.rate,sample_mode= nidaqmx.constants.AcquisitionType.CONTINUOUS)
        self.writer = nidaqmx.stream_writers.AnalogSingleChannelWriter(self.outputTask.out_stream, auto_start=False)
        self.signalFunction = self.signal_type(signalType)
        timePoints = np.linspace(0,1/frequency,int(self.rate/frequency))
        self.samples = self.signalFunction(timePoints,frequency)
    def start_acq(self):
        self.outputTask.start()
        self.writer.write_many_sample(self.samples)
        self.outputTask.wait_until_done(timeout=100)
    def stop_acq(self):
        self.outputTask.stop()
    def signal_type(self,value):
        if value == 0:
            return self.sawtooth_signal
    def sawtooth_signal(self,points,frequency):
        return signal.sawtooth(2*np.pi*frequency*points,width = 0.5)
    def change_value(self,frequency):
        self.stop_acq()
        timePoints = np.linspace(0,1/frequency,int(self.rate/frequency))
        self.samples = self.signalFunction(timePoints,frequency)
        self.start_acq()
        
if __name__ == "__main__":
    output = outputSignal("Dev1/ao0", 1000000,100)
    output.start_acq()
    time.sleep(10)
    #output.change_value(10)
    #time.sleep(10)
    output.outputTask.close()
