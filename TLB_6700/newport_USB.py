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

class newportUSBDevices(self):
    def __init__(self):
        self._devices = newport_USB_Devices(Newport.USBComm.USB())
        self._devices.OpenDevices()
        self._devices_info = self._devices.GetDevInfoList()
    def close_devices(self):
        self._devices.CloseDevices()
    def get_all_description(self):
        count = 0
        while (count< len(self._devices_info)):
            yield self._devices_info[count].get_Description()
            count += 1
    def get_description(self,device_number):
        return self._devices_info[device_number].get_Description()
        
            
        
        
