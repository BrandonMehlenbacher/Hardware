import pyvisa as visa
import sys
import numpy as np
from ThorlabsPM100 import ThorlabsPM100
import matplotlib.pyplot as plt
import matplotlib
import time
from datetime import datetime
import os
import pyqtgraph as pg


def printResources(resourceManager):
    for  resource in resourceManager.list_resources():
        try:
            #function came from instrumental documentation
            print(resource, '-->', rm.open_resource(resource).query('*IDN?').strip())
        except visa.VisaIOError:
            pass
    
class PowerMeter:
    def __init__(self,resource,duration='Endless'):
        self.resource = ThorlabsPM100(inst=resource)
        if duration == 'Endless':
            self.duration = 100000000
        else:
            self.duration = duration
        self.timeSpacing = 0.1
        self.valuesArray = np.zeros(shape = (2,int(self.duration/self.timeSpacing)+1))
    def run(self):
        currentTime = 0
        plt.xlabel("Time (s)")
        plt.ylabel("Power (mW)")
        count = 0 
        while currentTime < self.duration:
            try:
                currentValue = self.resource.read
                currentTime += self.timeSpacing
                self.valuesArray[0,count] = currentTime
                self.valuesArray[1,count] = currentValue*1000
                plt.plot(self.valuesArray[0,:count],self.valuesArray[1,:count],c='k')
                plt.pause(self.timeSpacing)
                count +=1
            except KeyboardInterrupt:
                plt.close()
                sys.exit()
                break
    def save(self,filename="data"):
        directory = str(datetime.now().date())
        new_trace = 1
        if self.duration > 10000000:
            print("I will not save this to a csv, I doubt it could handle that many values, also numpy is struggling to make that big of an array")
            return
        if not os.path.isdir(directory):
                os.makedirs(directory)
        new_file_description = directory+"/"+filename
        new_file = new_file_description
        while os.path.isfile(new_file+".csv"):
            new_file = new_file_description+f"_{new_trace}"
            new_trace +=1
        np.savetxt(new_file+".csv", self.valuesArray.transpose(),delimiter = ',')
if __name__ == "__main__":
    rm = visa.ResourceManager()
    #printResources(rm)
    resource = rm.open_resource('USB0::0x1313::0x8078::P0029177::INSTR')
    powerMeter = PowerMeter(resource, 1)
    powerMeter.run()
    powerMeter.save(filename = "monitorRedLaser")
    
            
            
            
