from ctypes import (c_int32, c_bool, byref, create_string_buffer, Structure, POINTER, oledll)
from enum import Enum
import time

lib=oledll.LoadLibrary('C:/Program Files/Software_ECC100/Software_ECC100_1.6.8/ECC100_DLL/Win64/ecc.dll')

    
class EccInfo(Structure):
    _fields_ = [('id',c_int32),('locked',c_bool)]

class ECC100Control:
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
        lines= []

        if message:
            lines.append(message)
        if func:
            lines.append(f"Error returned by {func}")
        print(retval)
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
        # this value is in mHz
        frequency = c_int32(int(frequency))
        ret = self.lib.ECC_controlFrequency(self.dev_handle,axis,byref(frequency),set)
        self.handle_err(ret,func="control_frequency ")
        return frequency.value

    def set_frequency(self,axis,value):
        self.control_frequency(axis,value,set=True)

    def get_frequency(self,axis):
        return self.control_frequency(axis)

    def control_move_feedback(self, axis,enable = False,set=False):
        enable = c_bool(enable)
        ret = self.lib.ECC_controlMove(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_move")
        return bool(enable.value)

    def control_continuous_forward(self,axis,enable=False,set=False):
        enable = c_bool(enable)
        ret = self.lib.ECC_controlContinousFwd(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_move")
        return bool(enable.value)

    def control_continuous_backward(self,axis,enable=False,set=False):
        enable = c_bool(enable)
        ret = self.lib.ECC_controlContinousBkwd(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_move")
        return bool(enable.value)

    def move_enabled_feedback(self,axis):
        self.control_move_feedback(axis,enable=True,set=True)

    def move_disable_feedback(self,axis):
        self.control_move_feedback(axis,enable=False,set=True)

    def move_status(self,axis):
        return self.control_move(axis)

    def get_position(self,axis):
        position = c_int32()
        ret = self.lib.ECC_getPosition(self.dev_handle,axis,byref(position))
        self.handle_err(ret,func="get_position")
        return position.value

    def move_target(self,axis,target= 0,set=False):
        target = c_int32(target)
        ret = self.lib.ECC_controlTargetPosition(self.dev_handle,axis,byref(target),set)
        self.handle_err(ret,func="move_to")
        return target.value

    def get_target(self,axis):
        return self.move_target(axis)

    def set_target(self,axis,target):
        return self.move_target(axis,target, set=True)       

    def move_range(self,axis,target= None,set=False):
        if target == None:
            return
        rangeVal = c_int32(rangeVal)
        ret = self.lib.ECC_controlTargetRange(self.dev_handle,axis,byref(rangeVal),set)
        self.handle_err(ret,func="move_range")
        return rangeVal.value

    def moving_status(self,axis):
        moving = c_int32()
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(moving),set)
        self.handle_err(ret,func="control_move")
        return moving.value
    
    def set_single_step(self,axis,backward):
        ret = self.lib.ECC_setSingleStep(self.dev_handle,axis,backward)
        self.handle_err(ret,func="set_single_step")

    def control_target_range(self,axis,targetRange=0, set=False):
        targetRange = c_int32(targetRange)
        ret = self.lib.ECC_controlTargetRange(self.dev_handle,axis,byref(targetRange),set)
        self.handle_err(ret,func="control_target_range")
        return targetRange.value

    def control_output(self,axis,enable=False, set=False):
        enable = c_bool(enable)
        ret = self.lib.ECC_controlOutput(self.dev_handle, axis, byref(enable), set)
        self.handle_err(ret, func = "control_output")
        return bool(enable.value)

    def enable_output(self,axis):
        self.control_output(axis,enable=True,set=True)

    def disable_output(self,axis):
        self.control_output(axis,enable=False,set=True)

    def wait_until_position(self,axis):
        targetRange = 1000#self.control_target_range(1)
        position = self.get_position(axis)
        targetPosition = self.get_target(axis)
        return abs(position-targetPosition)<=targetRange

    def is_moving_forward(self,axis):
        return self.control_continuous_forward(axis)

    def is_moving_backward(self,axis):
        return self.control_continuous_backward(axis)
    
    def move_to(self,axis,target=None):
        if target == None:
            raise ValueError("Must enter a value to move to a targeted position")
        self.move_enabled_feedback(axis)
        #self.control_target_range(axis,set=True)
        initialPosition = self.get_position(axis)
        targetPosition = self.get_target(axis)
        self.set_target(axis,target+initialPosition)
        targetPosition = self.get_target(axis)
        if self.wait_until_position(axis):
            return
        if initialPosition < targetPosition:
            print("forward it is")
            self.control_continuous_forward(1,enable=True,set=True)
        elif initialPosition > targetPosition:
            print("backward it is")
            self.control_continuous_backward(1,enable=True,set=True)
        self.enable_output(axis)
        while not self.wait_until_position(axis):
            pass
        self.stop_stepping(axis)

    def stop_stepping(self,axis):
        if self.is_moving_forward(axis):
            self.control_continuous_forward(1,enable=False,set=True)
        if self.is_moving_backward(axis):
            self.control_continuous_backward(1,enable=False,set=True)
    
    def close(self):
        ret = self.lib.ECC_Close(self.dev_handle)
        self.handle_err(ret,func="Close")
        
if __name__ == "__main__":
    ecc = ECC100Control()
    ecc.connect()
    ecc.set_amplitude(1,30000) #30 V
    ecc.set_frequency(1,100000)  # 100 Hz
    print(ecc.get_frequency(1))
    print(ecc.get_position(1))
    ecc.move_to(1,target=10000) # move 10 microns
    ecc.close()
