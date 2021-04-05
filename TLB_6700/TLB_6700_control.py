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
            print("there was an issue initalizing the controller, try unplugging the usb connection and plugging it back in. \nIf it is still broken talk to Brandon")
            sys.exit()
        self.set_IDs_Newport(self._controllers)
        
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

    def operation_completed(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'*OPC?',string)
        string = string.ToString()
        if string == "1":
            return True
        else:
            return False

    def get_actual_number_scans(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:WAVELENGTH?',string)
        string = string.ToString()
        self._number_scans = int(string.t)

    def output_state_laser(self,state):
        #if state is 1 the laser will be turned on if it is 0 the laser will be turned off
        self._newport_devices.Write(self._ID_list[0],f'OUTP:STAT {state}')
        
    def get_wavelength(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:WAVELENGTH?',string)
        string = string.ToString()
        self._current_wavelength = int(string)
        #just for debugging purposes
        print(self._current_wavelength)

    def get_current_diode(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:CURRENT:DIODE?',string)
        string = string.ToString()
        self._current = int(wavelength_string)
        
    def get_power_diode(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:POWER:DIODE?',string)
        string = string.ToString()
        self._power = int(wavelength_string)
        
    def change_wavelength(self,newWavelength):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH {newWavelength}')
        self.wavelength = newWavelength
        
    def change_state_lambda_track(self,state):
            self._newport_devices.Write(self._ID_list[0],f'OUTPUT:STATE {state}')

    def change_laser_power(self,power):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:POWER:DIODE {power}')

    def change_start_scan_wavelength(self,wavelength):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:START {wavelength}')
        
    def change_end_scan_wavelength(self,wavelength):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:END {wavelength}')
   
    def change_velocity_wavelength_change_forward(self,velocity):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:SLEW:FORWARD {velocity}')
        
    def change_velocity_wavelength_change_reverse(self,velocity):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:SLEW:REVERSE {velocity}')
        
    def change_number_scans(self,scans):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:DESSCANS {scans}')

    def change_mode_laser_power(self,state):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:CPOWER {state}')
        
    def start_scan(self):
        self._newport_devices.Write(self._ID_list[0],f'OUTPUT:SCAN:START')

    def end_scan(self):
        self._newport_devices.Write(self._ID_list[0],f'OUTPUT:SCAN:STOP')        

    def close_devices(self):
        self._newport_devices.CloseDevices()

if __name__ == '__main__':
    laser = TLB_6700_controller("SN41044")
    laser.current = 55
    settingChange = -1
    while settingChange != 20:
        settingChange = int(input("What would you like to do to the laser? \n 1: Turn On \n 2: Turn Off \n 3: Start Scan \n 4: Print Wavelength \n 5: Change Wavelength"))
        if settingChange == 1:
            laser.output_state_laser(1)
        elif settingChange == 2:
            laser.output_state_laser(0)
        elif settingChange == 3:
            laser.start_scan(1)
        elif settingChange == 4:
            print(laser.wavelength)
        elif settingChange == 5:
            laser.change_wavelength(780.00)
        elif settingChange ==6:
            laser.operation_completed()
    laser.close_devices()
