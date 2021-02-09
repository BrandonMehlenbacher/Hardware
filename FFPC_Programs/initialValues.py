import csv
import pathlib
import os
import sys

class initializeValues(object):
    """
    One of the hallmark features of labview is the ability to be able to change the current value
    to be the initialized value on start up. This makes it easy to start and stop. This class is designed
    as an attempt to imitate that feature.

    Inputs:
    names: these are the names of all the variables you want to keep track of,
    future note I want to make a program to scan the file to find all switchable buttons and do it the easy way
    filename: what you want your file to be called, needs to be a csv file as of now

    Outputs:
    an intializeValues object that behaves similarly to a dictionary with added features
    """
    
    def __init__(self,names,filename='initialValues.csv'):
        # changes current working directory to location of python file
        os.chdir(os.path.abspath(os.path.dirname(sys.argv[0]))) 
        self.filename = filename
        self.names = names
        self.initialValues = self.getInitialValues(names)

    def getInitialValues(self,names):
        """
        Inputs:
        names: names of the variables you want to keep track of over a long period of time

        Output:
        a dictionary which can be used to access the values
        """
        currentDict = dict()
        path = pathlib.Path(self.filename)
        # determines if the filename already exists, if it does then it reads the values,
        # if it doesn't then it will force you to input the values you want to start with
        if path.is_file():
            with open(self.filename,mode='r',newline='') as file:
                reader = csv.reader(file,delimiter=',')
                for name, value in reader:
                    currentDict[name] = value
        else:
            for name in names:
                value = float(input(f"For {name} what do you want the saved value? "))
                currentDict[name] = value
            self.saveValues(None,currentDict = currentDict)
        return currentDict

    def listEntries(self):
        for name,value in self.initialValues.items():
            print(name,value)

    def getEntry(self,name):
        if name in self.initialValues.keys():
            return float(self.initialValues[name])
        else:
            sys.exit("value does not exist, please make sure you entered everything correctly")

    def changeValues(self,values):
        nameList = self.names
        for i in range(len(nameList)):
            self.initialValues[nameList[i]] = values[i]
            
    def saveValues(self,values,currentDict=None):
        """
        Saves the values in a csv document
        """
        path = pathlib.Path(self.filename)
        if path.is_file():
            self.changeValues(values)
            savedDict = self.initialValues
        else:
            savedDict = currentDict
        with open(self.filename,'w',newline = '') as file:
            writer = csv.writer(file,delimiter=',')
            for name,value in savedDict.items():
                writer.writerow([name,value])
        self._is_file = True

if __name__ == "__main__":
    initializer = initializeValues()
    initializer.listEntries()
    values = [1,2,3,4]
    initializer.changeValues(values)
    initializer.listEntries()
    initializer.saveValues()
        
