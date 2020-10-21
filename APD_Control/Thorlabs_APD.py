import nidaqmx
import numpy as np
import matplotlib.pyplot as plt


class APD_Reader(object):
    """
    the main idea for this class is to provide a generic APD reader
    it requires only one input, the channel that you are reading off of
    """
    def __init__(self,channel,size_of_channel,max_val = 2, min_val = -0.5):
        """
        Inputs:
        Channel: this is the input channel that we use must contain Dev
        Example: channel = "Dev1/ai0"

        """
       # nidaqmx.Task().timing.cfg_samp_clk_timing(rate = 1000000,sample_mode = nidaqmx.constants.AcquisitionType.CONTINUOUS)
        self._apd = nidaqmx.Task()
        self._apd.ai_channels.add_ai_voltage_chan(channel,max_val = max_val,min_val = min_val)
        self._rate = 1000000
        self._size_of_channel = size_of_channel
        self._apd.timing.cfg_samp_clk_timing(rate = self._rate,samps_per_chan = self._size_of_channel, sample_mode = nidaqmx.constants.AcquisitionType.CONTINUOUS)
        #self._apd.read(number_of_samples_per_channel = self._size_of_channel)
    @property
    def size_of_channel(self):
        return size_of_channel
    @size_of_channel.setter
    def size_of_channel(self,size):
        self._size_of_channel = size
    def start_acquisition(self):
        self._apd.start()
    def stop_acquisition(self):
        self._apd.stop()
    def close_daq(self):
        self._apd.close()
    def read_values(self):
        values = self._apd.read(number_of_samples_per_channel = nidaqmx.constants.READ_ALL_AVAILABLE)
        return values
    
if (__name__ == '__main__'):
    channel = 'Dev1/ai1'
    size = 100
    apd = APD_Reader(channel,size)
    apd.start_acquisition()
    print(apd.read_values())
    apd.stop_acquisition()
    apd.close_daq()
    
