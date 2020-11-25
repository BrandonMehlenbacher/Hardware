import thorlabs_apt as apt
import numpy as np
import argparse


class Motor(object):
    """
    This class will be used for controlling the various motors we have in lab.
    This is originally designed to work with any apt motor that we currently use
    in the resonator projects but can be modified later to incorporate other
    motors
    """
    def __init__(self,serial_number):
        """
        The serial number is the serial number of the motor. The thorlabs apt
        software i am using has it such that the serial number is the main idea
        around it. For newport motors, I believe it is a USB extension so this would
        have to be extended to that later
        """
        self._motor = None
        self._serial_number = None
        self._current_position = 0
        for values in apt.list_available_devices():
            if serial_number == values[1]:
                self._motor = apt.Motor(serial_number)
                self._serial_number = serial_number
        if self._motor == None:
            print("Input an invalid serial number")
    def attached_devices(self):
        print(apt.list_available_devices())
    def home(self):
        self._motor.move_home(True)
    def move_absolute(self,distance):
        self._motor.move_to(distance)
        self._current_position = self._motor.position
    def move_relative(self,distance):
        self._motor.move_by(distance)
        self._current_position = self._motor.position
    @property
    def position(self):
        return self._current_position
    @property
    def serial_number(self):
        return self._serial_number
    def enable(self):
        self._motor.enable()
    def disable(self):
        self._motor.disable()
