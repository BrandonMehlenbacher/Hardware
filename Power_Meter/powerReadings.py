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
import click


def printResources(resourceManager):
    for  resource in resourceManager.list_resources():
        try:
            #function came from instrumental documentation
            print(resource, '-->', rm.open_resource(resource).query('*IDN?').strip())
        except visa.VisaIOError:
            pass
    
class PowerMeter:
    """
    This class is designed for reading values from a Thorlabs power meter

    Inputs:
    resource: the opened visa resource from the computer
    duration: how long you want to collect data for
    averagingTime: how long do you want to average your data for
    timeSpacing: the distance between each point collected

    """
    def __init__(self,resource,duration='Endless',averagingTime = 1,timeSpacing=0.1):
        assert timeSpacing > 0.001, "We can only read the data points so fast, be patient"
        self.resource = ThorlabsPM100(inst=resource)
        self.averageTime = averagingTime 
        if duration == 'Endless':
            self.duration = 100000000
        else:
            self.duration = duration
        self.timeSpacing = 0.1 #how fast to collect the data
        self.valuesArray = np.zeros(shape = (2,int(self.duration/self.averageTime)+1))
    def run(self,filename):
        """
        Starts the acquisition sequence, creates a plot and automatically updates it as more data is collected
        """
        avgReading = []
        currentTime = 0
        arrayCounter = 0
        plt.xlabel("Time (s)")
        plt.ylabel("Power (mW)")
        while currentTime < self.duration:
            try:
                currentValue = self.resource.read
                avgReading.append(currentValue)
                # the if else statements below work as the following
                # the first one checks to see if the length of AvgReading is 10 for 10 data points
                # the second checks to see if we are at the first iteration
                # the third should only ever be active at the first iteration
                # the reasoning behind this is the else statement will operate the fewest number of times improving overall efficiency
                # I also hate counter variables soooooo yeah
                if len(avgReading) == int(1/self.timeSpacing):
                    currentTime += self.averageTime
                    avgValue = sum(avgReading)/len(avgReading)
                    self.valuesArray[0,arrayCounter] = currentTime
                    self.valuesArray[1,arrayCounter] = avgValue*1000
                    plt.plot(self.valuesArray[0,:arrayCounter],self.valuesArray[1,:arrayCounter],c='k')
                    plt.pause(self.timeSpacing)
                    avgReading = []
                    arrayCounter +=1
                elif arrayCounter != 0:
                    time.sleep(self.timeSpacing)
                else:
                    self.valuesArray[0,arrayCounter] = currentTime
                    self.valuesArray[1,arrayCounter] = currentValue*1000 # changes the units to mW
                    plt.plot(self.valuesArray[0,:arrayCounter],self.valuesArray[1,:arrayCounter],c='k')
                    plt.pause(self.timeSpacing)
                    arrayCounter +=1
            except KeyboardInterrupt:
                plt.close()
                self.valuesArray = self.valuesArray[:,:arrayCounter]
                self.save(filename)
                sys.exit()
                break
        self.save(filename)
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
        if plt.fignum_exists(1):
            plt.close()

if __name__ == "__main__":
    rm = visa.ResourceManager()
    #printResources(rm)
    resource = rm.open_resource('USB0::0x1313::0x8078::P0021183::INSTR')
    timeDesired = int(input("Input the time you want to measure the power for, remember it only saves at the end: "))
    powerMeter = PowerMeter(resource, timeDesired)
    defaultFileName = click.prompt("Enter file name",type=str,default = "power780LaserHead_afterPolarizer")
    filename = f"{defaultFileName}_{timeDesired}s"
    powerMeter.run(filename)
    
            
            
            
