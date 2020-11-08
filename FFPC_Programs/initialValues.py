import csv
import pathlib

class initializeValues(object):
    def __init__(self,names,filename='initialValues.csv'):
        self.filename = filename
        self.names = names
        self.initialValues = self.getInitialValues(names)
    def getInitialValues(self,names):
        currentDict = dict()
        path = pathlib.Path(self.filename)
        if path.is_file():
            with open(self.filename,mode='r',newline='') as file:
                reader = csv.reader(file,delimiter=',')
                for name, value in reader:
                    currentDict[name] = value
        else:
            valuesList = []
            for name in names:
                value = int(input(f"For {name} what do you want the saved value? "))
                currentDict[name] = value
                valuesList.append(value)
            self.saveValues(valuesList)
        return currentDict
    def listEntries(self):
        for name,value in self.initialValues.items():
            print(name,value)
    def getEntry(self,name):
        if name in self.initialValues.keys():
            return self.initialValues[name]
        else:
            sys.exit("value does not exist, please make sure you entered everything correctly")
    def changeValues(self,values):
        nameList = self.names
        for i in range(len(nameList)):
            print(nameList[i])
            self.initialValues[nameList[i]] = values[i]
    def saveValues(self,values):
        self.changeValues(values)
        with open(self.filename,'w',newline = '') as file:
            writer = csv.writer(file,delimiter=',')
            for name,value in self.initialValues.items():
                writer.writerow([name,value])

if __name__ == "__main__":
    initializer = initializeValues()
    initializer.listEntries()
    values = [1,2,3,4]
    initializer.changeValues(values)
    initializer.listEntries()
    initializer.saveValues()
        
