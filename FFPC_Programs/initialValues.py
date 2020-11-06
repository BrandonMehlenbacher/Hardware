import csv
import pathlib

class initializeValues(object):
    def __init__(self,filename='initialValues.csv'):
        self.filename = filename
        self.initialValues = self.getInitialValues()
    def getInitialValues(self):
        currentDict = dict()
        path = pathlib.Path(self.filename)
        if path.is_file():
            with open(self.filename,mode='r',newline='') as file:
                reader = csv.reader(file,delimiter=',')
                for name, value in reader:
                    currentDict[name] = value
        else:
            num_entries = int(input("How many values do you want to be saved? "))
            for x in range(num_entries):
                name = input("Name of value? ")
                value = int(input("Saved Value? "))
                if name in currentDict.keys():
                    print("Only one entry per key name")
                currentDict[name] = value
        return currentDict
    def listKeys(self):
        nameList = []
        for name in self.initialValues.keys():
            nameList.append(name)
        return nameList
    def listEntries(self):
        for name,value in self.initialValues.items():
            print(name,value)
    def getEntry(self,name):
        if name in self.initialValues.keys():
            return self.initialValues[name]
        else:
            sys.exit("value does not exist, please make sure you entered everything correctly")
    def changeValues(self,values):
        nameList = self.listKeys()
        for i in range(len(nameList)):
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
        
