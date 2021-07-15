from ctypes import (c_int32, c_bool, byref, create_string_buffer, Structure, POINTER, oledll)
from enum import Enum
import time

lib=oledll.LoadLibrary('C:/Program Files/Software_ECC100_1.6.8/ECC100_DLL/Win64/ecc.dll') # this is the path to the ecc.dll, if becoming a package easily can be modified

    
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
        """
        determines if there is a device connected to the computer
        """
        info = POINTER(EccInfo)()
        num = self.lib.ECC_Check(byref(info))
        info_list = [info[i] for i in range(num)]
        return num, info_list

    def connect(self):
        """
        Connects to the first device on the computer
        """
        handle = c_int32()
        ret = self.lib.ECC_Connect(self.dev_num,byref(handle))
        self.dev_handle = handle.value
        self.handle_err(ret,func="Connect")
        self.dev_handle = handle.value
        
    def handle_err(self, retval, message = None, func = None):
        """
        Handles errors that come up while using the instrument
        """
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
        """
        Controls the amplitude of the attocube
        Units are in mV so to set to 30 V must be 30000 mV
        """
        amplitude = c_int32(int(amplitude))
        ret = self.lib.ECC_controlAmplitude(self.dev_handle,axis,byref(amplitude),set)
        self.handle_err(ret,func="control_amplitude")
        return amplitude.value

    def get_amplitude(self,axis):
        """
        Gets the set amplitude of the attocube, units are in mV
        """
        return self.control_amplitude(axis)
    
    def set_amplitude(self,axis,value):
        """
        Sets the amplitude of the attocube, units are in mV
        """
        self.control_amplitude(axis,value,set=True)

    def control_frequency(self, axis,frequency = 0,set=False):
        """
        Controls the frequency of the attocube, units are in mHz so to set 100 Hz must be 100000 mHz
        """
        # this value is in mHz
        frequency = c_int32(int(frequency))
        ret = self.lib.ECC_controlFrequency(self.dev_handle,axis,byref(frequency),set)
        self.handle_err(ret,func="control_frequency ")
        return frequency.value

    def get_frequency(self,axis):
        """
        Gets the frequency of the attocube, units are in mHz
        """
        return self.control_frequency(axis)

    def set_frequency(self,axis,value):
        """
        Sets the frequency of the attocube, units are in mHz
        """
        self.control_frequency(axis,value,set=True)



    def control_move_feedback(self, axis,enable = False,set=False):
        """
        Controls if the attocube is moving under closed loop feedback
        """
        enable = c_bool(enable)
        ret = self.lib.ECC_controlMove(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_move")
        return bool(enable.value)

    def move_enabled_feedback(self,axis):
        """
        Enables closed loop feedback for moving attocube
        """
        self.control_move_feedback(axis,enable=True,set=True)

    def move_disable_feedback(self,axis):
        """
        Disables closed loop feedback for moving attocube
        """
        self.control_move_feedback(axis,enable=False,set=True)

    def move_status(self,axis):
        """
        Gets the current status of the movement
        """
        return self.control_move(axis)

    def control_continuous_forward(self,axis,enable=False,set=False):
        """
        Allows for attocube to move forward
        """
        enable = c_bool(enable)
        ret = self.lib.ECC_controlContinousFwd(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_continuous_forward")
        return bool(enable.value)

    def is_moving_forward(self,axis):
        """
        Checks if the attocube is moving forward
        """
        return self.control_continuous_forward(axis)

    def control_continuous_backward(self,axis,enable=False,set=False):
        """
        Allows for attocube to move backward
        """
        enable = c_bool(enable)
        ret = self.lib.ECC_controlContinousBkwd(self.dev_handle,axis,byref(enable),set)
        self.handle_err(ret,func="control_continuous_backward")
        return bool(enable.value)

    def is_moving_backward(self,axis):
        """
        Checks if the attocube is moving backwards
        """
        return self.control_continuous_backward(axis)

    def stop_stepping(self,axis):
        """
        Stops the attocube from moving forward or backward, depending on which is active
        """
        if self.is_moving_forward(axis):
            self.control_continuous_forward(1,enable=False,set=True)
        if self.is_moving_backward(axis):
            self.control_continuous_backward(1,enable=False,set=True)

    def get_position(self,axis):
        """
        Gets the current relative position of the attocube (Note I said relative, the attocube does not do absolute positioning)
        """
        position = c_int32()
        ret = self.lib.ECC_getPosition(self.dev_handle,axis,byref(position))
        self.handle_err(ret,func="get_position")
        return position.value

    def move_target(self,axis,target= 0,set=False):
        """
        Controls the target of the attocube, this is relative to the original 0 so for instance going from 0 to 10 microns you would set 10000, then 20000 to move to 20 microns not 10 microns again
        units are in nm so to move 1 micron must be set to 1000 nm
        """
        target = c_int32(target)
        ret = self.lib.ECC_controlTargetPosition(self.dev_handle,axis,byref(target),set)
        self.handle_err(ret,func="move_to")
        return target.value

    def get_target(self,axis):
        """
        Gets the target position
        """
        return self.move_target(axis)

    def set_target(self,axis,target):
        """
        Sets the target position
        """
        return self.move_target(axis,target, set=True)       

    def move_range(self,axis,rangeVal= None,set=False):
        """
        Changes the target range in which the motor is said to be at the correct spot
        I leave it at 0 so that the feedback works correctly
        """
        if rangeVal == None:
            return
        rangeVal = c_int32(rangeVal)
        ret = self.lib.ECC_controlTargetRange(self.dev_handle,axis,byref(rangeVal),set)
        self.handle_err(ret,func="move_range")
        return rangeVal.value
    
    def set_single_step(self,axis,backward):
        """
        Allows for a single step to be taken, I currently do not use this but it seems to be worth while
        """
        ret = self.lib.ECC_setSingleStep(self.dev_handle,axis,backward)
        self.handle_err(ret,func="set_single_step")

    def control_output(self,axis,enable=False, set=False):
        """
        Allows for movement of the attocube, can be switched from off to on
        """
        enable = c_bool(enable)
        ret = self.lib.ECC_controlOutput(self.dev_handle, axis, byref(enable), set)
        self.handle_err(ret, func = "control_output")
        return bool(enable.value)

    def enable_output(self,axis):
        """
        Enables output of the attocube
        """
        self.control_output(axis,enable=True,set=True)

    def disable_output(self,axis):
        """
        Disables output of the attocube
        """
        self.control_output(axis,enable=False,set=True)

    def wait_until_position(self,axis,targetRange=1000):
        """
        Determines if the attocube is close at the correct position
        """
        targetRange = targetRange#self.control_target_range(1)
        position = self.get_position(axis)
        targetPosition = self.get_target(axis)
        return abs(position-targetPosition)<=targetRange


    
    def move_to(self,axis,target=None,targetRange= 1000):
        """
        Moves the attocube to the defined position
        """
        if target == None:
            raise ValueError("Must enter a value to move to a targeted position")
        self.move_enabled_feedback(axis)
        #self.control_target_range(axis,set=True)
        initialPosition = self.get_position(axis)
        targetPosition = self.get_target(axis)
        self.set_target(axis,target+initialPosition) #makes the target relative to the current position for easier use
        targetPosition = self.get_target(axis)
        if self.wait_until_position(axis):
            return
        if initialPosition < targetPosition:
            self.control_continuous_forward(1,enable=True,set=True)
        elif initialPosition > targetPosition:
            self.control_continuous_backward(1,enable=True,set=True)
        self.enable_output(axis)
        while not self.wait_until_position(axis,targetRange=targetRange):
            pass
        self.stop_stepping(axis)
    
    def close(self):
        """
        Terminates the connection to the attocube
        """
        ret = self.lib.ECC_Close(self.dev_handle)
        self.handle_err(ret,func="Close")

class Motor(ECC100Control):
    def __init__(self):
        super.__init__()

if __name__ == "__main__":
    ecc = ECC100Control()
    ecc.connect()
    ecc.set_amplitude(1,30000) #30 V
    ecc.set_frequency(1,100000)  # 100 Hz
    print(ecc.get_frequency(1))
    print(ecc.get_position(1))
    ecc.move_to(1,target=10000) # move 10 microns
    ecc.close()
