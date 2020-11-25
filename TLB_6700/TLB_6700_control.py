import sys
import os
import numpy as np
import platform
import os
from ctypes import *
import time

import clr
from System.Reflection import Assembly
from System.Text import StringBuilder
from System import Int32
from System.Collections import Hashtable
driver_path = 'C:\\Program Files\\Newport\\Newport USB Driver\\Bin\\UsbDllWrap.dll'
Assembly.LoadFile(driver_path)
clr.AddReference(r'UsbDllWrap')
import Newport

class TLB_6700_controller(object):
    def __init__(self,desiredLaser):
        self._newport_devices = Newport.USBComm.USB()
        self._desired_laser = desiredLaser
        self._newport_devices.OpenDevices(0, False)
        self._newport_device_info = self._newport_devices.GetDevInfoList()
        self._lasers_lab = ["SN18084","SN41044"] #this is a list of the laser controllers we have in lab
        self._ID_list = [1] #only able to use one laser until i figure out the issue with device key or ID
        self._controllers = self.controllers_list(self._newport_device_info)
        if len(self._controllers) == 0:
            print("there was an issue initalizing the controller")
            sys.exit()
        print(self._controllers)
        self.set_IDs_Newport(self._controllers)
        self._current_wavelength = 0
        self._current = 40 # this will be in mA
        self._turned_on = 0 #if any laser is turned on
        self._piezo_voltage = 0
        self._lasing_power = 0
        self._wavelength_range = [[]] # list of list of wavelength ranges for the lasers
        self._scanning_range = []
        #self.set_wavelength_range()
        #self.initialize_laser_conditions()
    def intialize_laser_conditions(self):
        pass
    def set_IDs_Newport(self,array_list):
        for x in range(len(array_list)):
            if (array_list[x].get_Description()[29:] == self._desired_laser):
                array_list[x].set_ID(1)
        """
        the idea for this code is to later implement control over both lasers instead of just one
        this is a work in progress as I have yet to figure out why it wont work
        for x in range(len(array_list)):
            if (array_list[x].get_Description()[29:] == self._lasers_lab[0]):
                array_list[x].set_ID(x+1)
                self._ID_list.append(x+1)
            elif (array_list[x].get_Description()[29:] == self._lasers_lab[1]):
                array_list[x].set_ID(x+1)
                self._ID_list.append(x+1)
        """
    def controllers_list(self,USB_controllers):
        controller_list = []
        for controller in range(len(USB_controllers)):
            if (USB_controllers[controller].get_Description()[29:] in self._lasers_lab):
                controller_list.append(USB_controllers[controller])
        return controller_list
    def set_wavelength_range(self):
        string_MIN = StringBuilder()
        string_MAX = StringBuilder()
        for x in range(len(array_list)):
            self._newport_devices.Query(self._ID_list[0],'SOUR:WAVE:MAX?',string_MAX)
            self._newport_devices.Query(self._ID_list[0],'SOUR:WAVE:MIN?',string_MIN)
            self._wavelength_range.append([string_MIN,string_MAX])
    def laser_status(self,status):
        """
        inputs:
        Status is whether the laser is turned on or turned off
        """
        self._newport_devices.Write(self._ID_list[0],f'OUTP:STAT {status}')
        self._turned_on = status
    def turnOn(self):
        self._newport_devices.Write(self._ID_list[0],f'OUTP:STAT {1}')
    def turnOff(self):
        self._newport_devices.Write(self._ID_list[0],f'OUTP:STAT {0}')
    @property
    def turned_on(self):
        return self._turned_on
    @property
    def wavelength(self):
        return self._current_wavelength
    @wavelength.setter
    def wavelength(self):
        wavelength_string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:WAVE?',wavelength_string)
        self._current_wavelength = int(wavelength_string)
    @property
    def lasing_power(self):
        return self._lasing_power
    def lasing_power(self,power):
        power_string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],f'SOURCE:POWER:DIODE {power}',power_string)
        self._lasing_power = int(power_string)
    @property
    def current(self):
        return self._current
    @current.setter
    def current(self,desired_current):
        """
        Inputs:
        desired current: this is the current (or power) desired from the laser, enter in mA
        """
        current_string = StringBuilder()
        desired_current = desired_current #this allows user to enter the value in mA
        #self._newport_devices.Query(self._ID_list[0],f'SOURCE:CURRENT:DIODE {desired_current}',current_string)
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:CURRENT:DIODE {desired_current}')
        self._current = desired_current
    @property
    def scanning_range(self):
        print(f"The scan starts at {self._scanning_range[0]} and ends at {self._scanning_range[1]}")
        return self._scanning
    @scanning_range.setter
    def scanning_range(self,start,end):
        start_scan = StringBuilder()
        end_scan = StringBuilder()
        if start < self._wavelength_range[0]:
            print(f"Start is less than the minimum range {self._wavelength_range[0]}, input valid number")
            exit()
        elif end > self._wavelength_range[1]:
            print(f"Start is greater than the maximum range {self._wavelength_range[1]}, input valid number")
            exit()
        self._newport_devices.Query(self._ID_list[0],f'SOURCE:WAVE:START {start}',start_scan)        
        self._newport_devices.Query(self._ID_list[0],f'SOURCE:WAVE:STOP {end}',end_scan)
        self._scanning_range = [int(start_scan),int(end_scan)]
    @property
    def piezo_voltage(self):
        return self._piezo_voltage
    @piezo_voltage.setter
    def piezo_voltage(self,volt):
        voltage_string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],f'SOURCE:VOLTAGE:PIEZO {volt}',voltage_string)
        self._piezo_voltage = int(volt_string)
    def start_scan(self,number_of_scans):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVE:DESSCANS {number_of_scans}')
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVE:START')
    def close_devices(self):
        self._newport_devices.CloseDevices()
#new_port_devices = Newport.USBComm.USB()

lasers = ["SN18084","SN41044"]
def set_IDs_Newport(array_list):
    for x in range(len(array_list)):
        print(array_list[x].get_Description())
        """
        if (array_list[x].get_Description()[29:] == lasers[0]):
            array_list[x].set_ID(0)
        elif (array_list[x].get_Description()[29:] == lasers[1]):
              array_list[x].set_ID(1)
        """
#my_array = []
#new_port_devices = Newport.USBComm.USB()
#device_key = '6700 SN18084'
#my_device.OpenDevices("New_Focus 6700 v2.4 03/19/14 SN41044",usingDeviceKey = True)
#new_port_devices.OpenDevices(device_key,usingDeviceKey=True)
#print(len(new_port_device_info))

#set_IDs_Newport(new_port_device_info)
#my_device.OpenDevices(0x100A)
#my_table = Hashtable()
#my_device.GetDeviceTable()
#print(my_device.GetDeviceTable())

#my_device.OpenDevices(myString,usingDeviceKey = True)
#my_device.get_Description()

#my_array = my_device.GetDevInfoList()
#help(my_array[0])
#my_array[0])

#set_IDs_Newport(my_array)
#string = StringBuilder()
#time.sleep(1)

#device = "6700SN18084"
#print(string)

#my_device.Write(1,'OUTP:STAT {1}')
#time.sleep(3)
#my_device.Write(0,'OUTP:STAT {1}')
#time.sleep(20)
#my_device.Write(1,'OUTP:STAT {0}')
#time.sleep(3)
#my_device.Write(0,'OUTP:STAT {0}')
#new_port_devices.CloseDevices()

if __name__ == '__main__':
    laser = TLB_6700_controller("SN41044")
    laser.current = 55
    #time.sleep(1)
    #print(laser.current)
    laser.turnOn()
    time.sleep(20)
    laser.turnOff()
    time.sleep(10)
    laser.close_devices()

