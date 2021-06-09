from ctypes import (c_int32, c_bool, byref, create_string_buffer, Structure, POINTER, oledll)
from enum import Enum


lib=oledll.LoadLibrary('C:/Program Files/Software_ECC100/Software_ECC100_1.6.8/ECC100_DLL/Win64/ecc.dll')

    
class EccInfo(Structure):
    _fields_ = [('id',c_int32),('locked',c_bool)]

class ECCControl:
    """
    Most of this work is based off of the instrumental-lib library implementation and I am just rewriting it so I do not have to use their package
    Please check their project out, I use a lot of their modules and it is amazing https://github.com/mabuchilab/Instrumental
    """
    def __init__(self):
        self.lib = lib
        num, info  = self.check()
        self.dev_num = 0
        if num < 1:
            raise Exception("No Devices Detected")
        
    def check(self):
        info = POINTER(EccInfo)()
        num = self.lib.ECC_Check(byref(info))
        info_list = [info[i] for i in range(num)]
        return num, info_list

    def connect(self):
        handle = c_int32()
        ret = self.lib.ECC_Connect(self.dev_num,byref(handle))
        self.dev_handle = handle.value
        self.handle_err(ret,func="Connect")
        self.dev_handle = handle.value
        
    def handle_err(self, retval, message = None, func = None):
        if retval == 0:
            return
        line= []

        if message:
            lines.append(message)
        if func:
            lines.append(f"Error returned by {func}")

        raise Exception("\n".join(lines))
    def control_amplitude(self, axis,amplitude = 0,set=False):
        amplitude = c_int32(int(amplitude))
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(amplitude),set)
        self.handle_err(ret,func="control_amplitude")
        return amplitude.value

    def get_amplitude(self,axis):
        return self.control_amplitude(axis)
    
    def set_amplitude(self,axis,value):
        self.control_amplitude(axis,value,set=True)

    def control_frequency(self, axis,frequency = 0,set=False):
        frequency = c_int32(int(frequency))
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(frequency),set)
        self.handle_err(ret,func="control_frequency ")
        return frequency.value

    def set_frequency(self,axis,value):
        self.control_frequency(axis,value,set=True)

    def get_frequency(self,axis):
        return self.control_frequency(axis)

    def control_move(self, axis,enable = False,set=False):
        enable = c_bool(enable)
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_move")
        return bool(enable.value)

    def move_enabled(self,axis):
        self.control_move(axis,enable=True,set=True)

    def move_disable(self,axis):
        self.control_move(axis,enable=False,set=True)

    def move_status(self,axis):
        return self.control_move(axis)

    def get_position(self,axis):
        position = c_int32()
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(position))
        self.handle_err(ret,func="get_position")
        return position.value

    def move_to(self,axis,target= None,set=False):
        if target == None:
            return
        target = c_int32(target)
        ret = self.lib.ECC_controlTargetRange(self.dev_handle,axis,byref(target),set)
        self.handle_err(ret,func="move_to")
        return target.value

    def moving_status(self,axis):
        moving = c_int32()
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(moving),set)
        self.handle_err(ret,func="control_move")
        return moving.value

if __name__ == "__main__":
    ecc = ECCControl()
    print(ecc.check())
    ecc.connect()
    print(ecc.get_amplitude(1))
    ecc.set_amplitude(1,30000)
    print(ecc.get_amplitude(1))