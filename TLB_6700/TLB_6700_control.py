import sys
import os
import numpy as np
import platform
import os
from ctypes import (c_int32, c_bool, byref, create_string_buffer, POINTER, oledll, c_wchar_p, c_char_p ,c_ulong)
import time

#import clr
#from System.Reflection import Assembly
#from System.Text import StringBuilder
#from System import Int32
#from System.Collections import Hashtable
#driver_path = 'C:/Program Files/Newport/Newport USB Driver/Bin/UsbDllWrap.dll'
#driver_path = 'C:/Program Files/Newport/Newport USB Driver/Bin/usbdll.dll'
driver_path = 'C:/WINDOWS/system32/usbdll.dll'
lib = oledll.LoadLibrary(driver_path)
#Assembly.LoadFile(driver_path)
#clr.AddReference(r'UsbDllWrap')
#import Newport
"""
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

        #the idea for this code is to later implement control over both lasers instead of just one
        #this is a work in progress as I have yet to figure out why it wont work
        #for x in range(len(array_list)):
         #   if (array_list[x].get_Description()[29:] == self._lasers_lab[0]):
         #       array_list[x].set_ID(x+1)
          #      self._ID_list.append(x+1)
          #  elif (array_list[x].get_Description()[29:] == self._lasers_lab[1]):
           #     array_list[x].set_ID(x+1)
             #   self._ID_list.append(x+1)

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
        
    def get_output_state_laser(self):
        #if state is 1 the laser will be turned on if it is 0 the laser will be turned off
        argument = f'OUTP:STAT?\n'
        self.buffer.Clear()
        self._newport_devices.Query(self._ID_list[0],f'OUTP:STAT?\n',self.buffer)
        string = self.buffer.ToString()
        if string == "0":
            return False
        else:
            return True
        
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

    def change_laser_current(self,power):
        self.buffer.Clear()
        argument = f'SOUR:CURR:DIOD {power}\n'
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
        argument = f'SOUR:WAVE:SLEW:RET {velocity}\n'
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
"""
class TLB_6700_controller(object):
    
    def __init__(self,serialNumber):
        self._lib = lib
        self.usb_init_system()
        self._device = self.get_instrument_list()
        
    def _handle_error(self,value):
         if value != 0:
             print("there was an error that occurred, please implement a better error system later")
             
    def get_instrument_list(self):
        arInstruments = POINTER(c_int32)()
        arInstrumentsModel = POINTER(c_int32)()
        arInstrumentsSN = POINTER(c_int32)()
        nArraySize = POINTER(c_int32)()
        value = self._lib.GetInstrumentList(byref(arInstruments),byref(arInstrumentsModel),byref(arInstrumentsSN),byref(nArraySize))
        self._handle_error(value)
        return None
        
    def usb_get_device_count(self):
        pass
    
    def usb_get_devive_key_from_device_id(self):
        pass
    
    def usb_dget_device_keys(self):
        pass
    
    def usb_get_os_name(self):
        buffer  = create_string_buffer(64)
        err = self._lib.newp_usb_GetOsName(buffer)
        self._handle_error(err)
        
    def usb_set_logging(self, logging: bool):
        logging = c_bool(logging)
        err = self.newp_usb_SetLogging(logging)
        self._handle_error(err)
    
    def usb_set_tracelog(self, log: bool):
        log = c_bool(logging)
        err = self.newp_usb_SetTraceLog(log)
        self._handle_error(err)
    
    def usb_event_assign_key(self):
        pass
    
    def usb_event_get_attached_devices(self):
        pass
    
    def usb_event_get_key_from_handle(self):
        pass
    
    def usb_event_init(self):
        pass
    
    def usb_event_remove_key(self):
        pass
    
    def usb_get_ascii(self):
        pass
    
    def usb_get_ascii_by_deviceID(self):
        pass
    
    def usb_get_device_info(self):
        pass
    
    def usb_get_model_serial_keys(self):
        pass
    
    def usb_init_system(self):
        err = self._lib.newp_usb_init_system()
        self._handle_error(err)
        
    def usb_init_product(self,productID: int):
        productID = c_int32(productID)
        err = self._lib.newp_usb_init_product(byref(productID))
        self._handle_error(err)
        
    def usb_open_devices(self,productID: int,UseUSBAddress: bool):
        productID = c_int32(productID)
        useUSBAddress = c_bool(UseUSBAddress)
        nNumDevices = POINTER(c_int32)()
        err = self._lib.newp_usb_open_devices(byref(productID),byref(useUSBAddress),byref(nNumDevices))
        self._handle_error(err)
        
    def usb_read_ascii_by_key(self):
        pass
    
    def usb_read_by_key(self):
        pass
    
    def usb_send_ascii(self,deviceID: int, command: str):
        length = len(command)+1 #have to take into account the carriage return
        deviceID = c_int32(deviceID)
        command = c_wchar_p(command)
        length = c_ulong(length)
        err = self._lib.newp_usb_send_ascii(byref(deviceID),byref(command),byref(length))
        self._handle_error(err)
        
    def usb_send_binary(selfdeviceID: int, command: bytes):
        length = len(command)+1 #have to take into account the carriage return
        deviceID = c_int32(deviceID)
        command = c_char_p(command)
        err = self._lib.newp_usb_send_ascii(byref(deviceID),byref(command),byref(length))
        self._handle_error(err)
        
    def usb_uninit_system(self):
        err = self._lib.newp_usb_unint_system()
        self._handle_error(err)
        
    def usb_write_binary_by_key(self):
        pass
    
    def usb_write_by_key(self):
        pass
    
        

if __name__ == '__main__':
    laser = TLB_6700_controller("SN41044")
    
