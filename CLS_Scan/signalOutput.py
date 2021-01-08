import nidaqmx
import numpy as np
from scipy import signal
from nidaqmx import *
import time
from PySide2.QtCore import QRunnable, Signal, QObject,QThread
"""
test_Task = nidaqmx.Task()
test_Task.ao_channels.add_ao_voltage_chan('Dev1/ao0')
frequency = 100
rate = 1000000
test_Task.timing.cfg_samp_clk_timing(rate=rate,sample_mode= nidaqmx.constants.AcquisitionType.CONTINUOUS)
test_Writer = nidaqmx.stream_writers.AnalogSingleChannelWriter(test_Task.out_stream, auto_start=True)
timePoints = np.linspace(0,1/frequency,int(rate/frequency))
samples = signal.sawtooth(2*np.pi*frequency*timePoints,width = 0.5)
test_Writer.write_many_sample(samples)
test_Task.wait_until_done(timeout=100)
"""


class signalOutput:
    def __init__(self,channel,rate,frequency,amplitude= 1,offset=0,continuous = True,signalType=0):
        self.rate = rate
        self.frequency = frequency
        self.amplitude =amplitude
        self.outputTask = nidaqmx.Task()
        self.outputTask.ao_channels.add_ao_voltage_chan(channel)
        self.outputTask.timing.cfg_samp_clk_timing(rate=self.rate,samps_per_chan = 1000000, sample_mode= nidaqmx.constants.AcquisitionType.FINITE)
        
        self.signalFunction = self.signal_type(signalType)
        timePoints = np.linspace(0,1/frequency,int(self.rate/(self.frequency)))
        self.samples = self.signalFunction(timePoints,self.frequency,amplitude,offset=0)
    def start_acq(self):
        self.writer = nidaqmx.stream_writers.AnalogSingleChannelWriter(self.outputTask.out_stream, auto_start=True)
        #self.outputTask.start()
        #time.sleep(1/self.frequency)
        self.writer.write_many_sample(self.samples)
        self.outputTask.wait_until_done(timeout=100)
    #def writeSamples(self):
        #self.writer.write_many_sample(self.samples)
    def stop_acq(self):
        self.outputTask.stop()
    def signal_type(self,value):
        if value == 0:
            return self.sawtooth_signal
    def sawtooth_signal(self,points,frequency,amplitude,offset):
        return signal.sawtooth(2*np.pi*frequency*points,width = 0.5)*amplitude+offset
    def change_value(self,frequency):
        self.stop_acq()
        timePoints = np.linspace(0,1/frequency,int(self.rate/frequency))
        self.samples = self.signalFunction(timePoints,frequency)
        self.start_acq()

class signals(QObject):
    terminate = Signal()

"""
for use with QRunnable
class workerOutput(QRunnable):
    def __init__(self,daq):
        super().__init__()
        self._daq = daq
        self.signals = signals()
        self.terminate = True
    def run(self):
        self._daq.start_acq()
        while self.terminate:
            pass
            #self._daq.start_acq()
        self._daq.stop_acq()
    def terminateLoop(self):
        self.terminate = False
"""
class workerOutput(QThread):
    def __init__(self,daq):
        QThread.__init__(self,None)
        self._daq = daq
        self.signals = signals()
        self.terminate = True
    def run(self):
        self._daq.start_acq()
        while self.terminate:
            self._daq.stop_acq()
            self._daq.start_acq()
        self._daq.stop_acq()
    def terminateLoop(self):
        self.terminate = False
if __name__ == "__main__":
    output = signalOutput("Dev1/ao0", 1000000,100)
    for x in range(10):
        output.start_acq()
        #time.sleep(10)
        output.stop_acq()
#    output.start_acq()
    
#output.start_acq()
     #   pass
        #print("hi")
        #output.start_acq()
        #output.stop_acq()
         #   break
    #time.sleep(10)
    #output.change_value(10)
    #time.sleep(10)
    #output.outputTask.close()

