import pyvisa as visa
import numpy as np
from ThorlabsPM100 import ThorlabsPM100
import matplotlib.pyplot as plt
import matplotlib
import time
import pyqtgraph as pg
#matplotlib.use('TkAgg')
def printResources(resourceManager):
    for  resource in resourceManager.list_resources():
        try:
            #function came from instrumental documentation
            print(resource, '-->', rm.open_resource(resource).query('*IDN?').strip())
        except visa.VisaIOError:
            pass

def update_line(myPlot,data):
    myPlot.set_xdata(np.append(myPlot.get_xdata(),data[0]))
    myPlot.set_xdata(np.append(myPlot.get_xdata(),data[1]))
    plt.draw()
    
class PowerMeter:
    def __init__(self,resource,duration='Endless'):
        self.resource = ThorlabsPM100(inst=resource)
        if duration == 'Endless':
            self.duration = 1000000000
        else:
            self.duration = duration
        self.timeSpacing = 0.1
        self.timeArray = []
        self.values = []
    def run(self):
        currentTime = 0
        plt.xlabel("Time (s)")
        plt.ylabel("Power (mW)")
        while currentTime < self.duration:
            try:
                currentValue = self.resource.read
                currentTime += self.timeSpacing
                self.timeArray.append(currentTime)
                self.values.append(currentValue*1000)
                #plt.scatter(currentTime,currentValue*1000)#,1,1,'.')
                plt.plot(self.timeArray,self.values,c='k')
                plt.pause(self.timeSpacing)
            except KeyboardInterrupt:
                plt.close()
                break
    def save(self):
        pass
if __name__ == "__main__":
    rm = visa.ResourceManager()
    #printResources(rm)
    resource = rm.open_resource('USB0::0x1313::0x8078::P0029177::INSTR')
    powerMeter = PowerMeter(resource,100)
    powerMeter.run()
    
            
            
            
