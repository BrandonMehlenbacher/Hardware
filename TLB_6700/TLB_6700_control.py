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
        self.buffer = StringBuilder(64)
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

    def query(self,argument):
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        return string
    
    def operation_completed(self):
        self.buffer.Clear()
        argument = '*OPC?\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string == "1":
            return True
        else:
            return False

    def check_lambda_track(self):
        argument = 'OUTP:TRAC?\n'
        self.buffer.Clear()
        if not self.status_byte:
            self.get_error_string()
            string = ""
        else:
            self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
            string = self.buffer.ToString()
        if string == "1":
            return True
        else:
            return False

    def get_actual_number_scans(self):
        string = self.buffer.Clear()
        argument = 'SOUR:WAVE:ACTSCANS?\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        try:
            return int(string)
        except ValueError:
            return 0

    def output_state_laser(self,state):
        #if state is 1 the laser will be turned on if it is 0 the laser will be turned off
        argument = f'OUTP:STAT {state}\n'
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],f'OUTP:STAT {state}\n',self.buffer)
        string = self.buffer.ToString()
        
    def get_wavelength(self):
        argument = 'SENS:WAVE?\n'
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        try:
            value = float(string)
            return value
        except ValueError:
            print(string)
                
    def status_byte(self):
        argument = '*STB?\n'
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string == "0":
            return True
        elif string == "1":
            return False
        
    def get_current_diode(self):
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],'SENS:CURR:DIOD?\n',self.buffer)
        string = self.buffer.ToString()
        try:
            return float(string)
        except ValueError:
            return 0
        
    def get_power_diode(self):
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],'SENS:POW:DIOD?\n',self.buffer)
        string = self.buffer.ToString()
        try:
            return float(string)
        except ValueError:
            return 0
        
    def change_wavelength(self,newWavelength):
        self.buffer.Clear()
        newWavelength = round(newWavelength,2)
        argument = f'SOUR:WAVE {newWavelength}\n' 
        if not self.status_byte:
            self.get_error_string()
        else:
            self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
            string = self.buffer.ToString()
        if string != "OK":
            print(string)
        
        
    def change_state_lambda_track_on(self):
            self.buffer.Clear()
            argument = 'OUTPUT:TRACK 1\n'
            if not self.status_byte:
                self.get_error_string()
                print("error checking change wavelength")
            elif self.operation_completed():
                self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
                string = self.buffer.ToString()
            else:
                string = ""
            if string != "OK":
               print(string)

    def change_state_lambda_track_off(self):
            self.buffer.Clear()
            argument = 'OUTPUT:TRACK 0\n'
            if not self.status_byte:
                self.get_error_string()
            else:
                self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
                string = self.buffer.ToString()
            if string != "OK":
               print(string)

    def change_laser_power(self,power):
        self.buffer.Clear()
        argument = f'SOUR:POW:DIOD {power}\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)

    def change_start_scan_wavelength(self,wavelength):
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],f'SOUR:WAVE:START {wavelength}\n',self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)
        
    def change_end_scan_wavelength(self,wavelength):
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],f'SOUR:WAVE:STOP {wavelength}\n',self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)
   
    def change_velocity_wavelength_change_forward(self,velocity):
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],f'SOUR:WAVE:SLEW:FORW {velocity}\n',self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)
        
    def change_velocity_wavelength_change_reverse(self,velocity):
        self.buffer.Clear()
        argument = f'SOURWAVE:SLEW:RET {velocity}\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)
        
    def change_number_scans(self,scans):
        self.buffer.Clear()
        argument = f'SOUR:WAVE:DESSCANS {scans}\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)

    def change_mode_laser_power(self,state):
        self.buffer.Clear()
        argument = f'SOUR:CPOW {state}\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)
        
    def start_scan(self):
        if self.check_lambda_track():
            self.buffer.Clear()
            argument = f'OUTP:SCAN:START\n'
            self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
            string = self.buffer.ToString()
            if string != "OK":
                print(string)

    def end_scan(self):
        self.buffer.Clear()
        argument = f'OUTP:SCAN:STOP\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)

    def close_devices(self):
        self._newport_devices.CloseDevices()
        time.sleep(1)

    def get_error_string(self):
        self.buffer.Clear()
        argument = 'ERRSTR?\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        print(string)
        
    def set_control_remote_mode(self,state):
        self.buffer.Clear()
        argument = f'SYST:MCON {state}\n'
        self._newport_devices.Query(self._ID_list[0],argument,self.buffer)
        string = self.buffer.ToString()
        if string != "OK":
            print(string)
        
if __name__ == '__main__':
    laser = TLB_6700_controller("SN41044")
    wavelength = 765.10
    settingChange = -1
    laser.set_control_remote_mode("REM")
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
            if not laser.check_lambda_track():
                laser.change_state_lambda_track_on()
                time.sleep(1)
            laser.change_wavelength(wavelength)
            if wavelength > 780:
                wavelength -= 1
            else:
                wavelength += 1
            time.sleep(1)
        elif settingChange ==6:
            laser.operation_completed()
        elif settingChange == 7:
            if laser.status_byte():
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
        elif settingChange == 11:
            laser.change_state_lambda_track_on()
        elif settingChange == 12:
            laser.change_state_lambda_track_off()
    laser.set_control_remote_mode("LOC")
    laser.close_devices()
