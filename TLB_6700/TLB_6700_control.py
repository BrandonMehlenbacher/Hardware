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
        self._newport_devices = Newport.USBComm.USB(bLogging=True)
        self._desired_laser = desiredLaser
        self._newport_devices.OpenDevices(0, False)
        self._newport_device_info = self._newport_devices.GetDevInfoList()
        self._lasers_lab = ["SN18084","SN41044"] #this is a list of the laser controllers we have in lab
        self._ID_list = [1] #only able to use one laser until i figure out the issue with device key or ID
        self._controllers = self.controllers_list(self._newport_device_info)
        if len(self._controllers) == 0:
            print("There was an issue initalizing the controller, try unplugging the usb connection and plugging it back in. \nIf it is still broken talk to Brandon")
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

    def successfully_get_value(self,argument,expected_string_length):
        count = 0
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],argument,string)
        string = string.ToString()
        while count <= 10**2:
            try:
                if len(string) <= expected_string_length and len(string) >=1:
                    
                    return string
            except ValueError:
                string = StringBuilder()
                self._newport_devices.Query(self._ID_list[0],argument,string)
                string = string.ToString()
                count +=1
                time.sleep(0.01)
        print("value unable to be read")
    
    def operation_completed(self):
        string = StringBuilder(64)
        self._newport_devices.Query(self._ID_list[0],'*OPC?\n',string)
        string = string.ToString()
        if string == "1":
            print(string)
            return True
        else:
            print(string)
            return False

    def get_actual_number_scans(self):
        #fix this
        string = StringBuilder(64)
        self._newport_devices.Query(self._ID_list[0],'SOURCE:WAVELENGTH:ACTSCANS?\n',string)
        string = string.ToString()
        self._number_scans = int(string)

    def output_state_laser(self,state):
        #if state is 1 the laser will be turned on if it is 0 the laser will be turned off
        self._newport_devices.Write(self._ID_list[0],f'OUTP:STAT {state}\n')
        
    def get_wavelength(self):
        expected_string_length = 7
        argument = 'SENSE:WAVELENGTH?\n'
        count = 0
        string = StringBuilder(64)
        self._newport_devices.Query(self._ID_list[0],argument,string)
        string = string.ToString()
        while count <= 10**2:
            try:
                if len(string) <= expected_string_length:
                    value = float(string)
                    return string
            except ValueError:
                string = StringBuilder(64)
                self._newport_devices.Query(self._ID_list[0],argument,string)
                string = string.ToString()
                count +=1
                time.sleep(0.01)
                
    def get_current_diode(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:CURRENT:DIODE?\n',string)
        string = string.ToString()
        self._current = int(wavelength_string)
        
    def get_power_diode(self):
        string = StringBuilder()
        self._newport_devices.Query(self._ID_list[0],'SENSE:POWER:DIODE?\n',string)
        string = string.ToString()
        self._power = float(wavelength_string)
        
    def change_wavelength(self,newWavelength):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH {newWavelength}\n')
        
    def change_state_lambda_track(self,state):
            self._newport_devices.Write(self._ID_list[0],f'OUTPUT:TRACK {state}\n')

    def change_laser_power(self,power):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:POWER:DIODE {power}\n')

    def change_start_scan_wavelength(self,wavelength):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:START {wavelength}\n')
        
    def change_end_scan_wavelength(self,wavelength):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:STOP {wavelength}\n')
   
    def change_velocity_wavelength_change_forward(self,velocity):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:SLEW:FORWARD {velocity}\n')
        
    def change_velocity_wavelength_change_reverse(self,velocity):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:SLEW:RETURN {velocity}\n')
        
    def change_number_scans(self,scans):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:WAVELENGTH:DESSCANS {scans}\n')

    def change_mode_laser_power(self,state):
        self._newport_devices.Write(self._ID_list[0],f'SOURCE:CPOWER {state}\n')
        
    def start_scan(self):
        self._newport_devices.Write(self._ID_list[0],f'OUTPUT:SCAN:START\n')

    def end_scan(self):
        self._newport_devices.Write(self._ID_list[0],f'OUTPUT:SCAN:STOP\n')        

    def close_devices(self):
        self._newport_devices.CloseDevices()
        time.sleep(1)

    def get_error_string(self):
        string = StringBuilder(64)
        self._newport_devices.Query(self._ID_list[0],'ERRSTR?\n',string)
        string = string.ToString()
        print(string)

if __name__ == '__main__':
    laser = TLB_6700_controller("SN41044")
    wavelength = 765.10
    settingChange = -1
    while settingChange != 20:
        settingChange = int(input("What would you like to do to the laser? \n 1: Turn On \n 2: Turn Off \n 3: Start Scan \n 4: Print Wavelength \n 5: Change Wavelength\n 6: Check Operation Complete\n 7: Get Wavelength \n 8: Change Number of Scans\n"))
        if settingChange == 1:
            laser.output_state_laser(1)
        elif settingChange == 2:
            laser.output_state_laser(0)
        elif settingChange == 3:
            laser.start_scan()
        elif settingChange == 4:
            laser.change_state_lambda_track(1)
        elif settingChange == 5:
            laser.change_wavelength(wavelength)
            wavelength += 0.01
            time.sleep(1)
        elif settingChange ==6:
            laser.operation_completed()
        elif settingChange == 7:
            value = laser.get_wavelength()
            print(value)
        elif settingChange == 8:
            laser.change_number_scans(10)
        elif settingChange == 9:
            laser.change_velocity_wavelength_change_forward(0.2)
            time.sleep(0.1)
            laser.change_velocity_wavelength_change_reverse(0.2)
        elif settingChange == 10:
            laser.get_error_string()
    laser.close_devices()
