# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:17:03 2020

@author: bmehl
"""

import ctypes
import numpy as np
from path import Path
from PyQt5 import QtCore
import matplotlib.pyplot as plt
import time
class CameraOpenError(Exception):
    def __init__(self, mesg):
        self.mesg = mesg
    def __str__(self):
        return self.mesg

class thorcam(QtCore.QThread):
    
    def __init__(self,filepath= Path('C:\\Program Files\\Thorlabs\\Scientific Imaging\\ThorCam\\uc480_64.dll'),
                 bit_depth=8,roi_shape=(1024,1024),exposure = 0.01, frame_rate = 10,
                 roi_pos = (0,0),memory=None):
        self.thorcam = ctypes.windll.LoadLibrary(filepath)
        #self.mem = None
        self.bit_depth = bit_depth
        self.handle = ctypes.c_int(0)
        init_camera = self.thorcam.is_InitCamera
        #init_camera.argtypes(ctypes.POINTER(ctypes.c_int))
        init_camera_failure = init_camera(ctypes.byref(self.handle))
        if init_camera_failure:
            raise CameraOpenError(f"Camera failed to open error code {init_camera_failure}")
        else:
            self.roi_shape = roi_shape
            self.frame_rate =  frame_rate
            self.roi_pos = roi_pos
            self.exposure = exposure
            self.memory = memory
        
        
# =============================================================================
#     def open_camera(self,):
#         init_camera = self.thorcam.is_InitCamera
#         init_camera.argtypes(ctypes.POINTER(ctypes.c_int))
#         init_camera_failure = init_camera(ctypes.byref(self.handle))
#         if init_camera_failure:
#             raise CameraOpenError(f"Camera failed to open error code {init_camera_failure}")
#         else:
#             
#             self.roi_shape = roi_shape
#             self.frame_rate =  frame_rate
#             self.roi_pos = roi_pos
#             self.exposure = exposure
# =============================================================================
    def start_video(self):
        self.thorcam.is_CaptureVideo(self.handle,1)
        
    def end_video(self):
        self.thorcam.is_StopLiveVideo(self.handle,1)
        
    @property
    def bit_depth(self):
        return self._bit_depth
    @bit_depth.setter
    def bit_depth(self,value):
        assert sum(int(item) for item in bin(value)[2:]) == 1, "bits need to be a multiple of 2"
        self._bit_depth = value
        
    
        
    @property
    def roi_shape(self):
        return self._roi_shape
    
    @roi_shape.setter
    def roi_shape(self,value):
        assert type(value)== tuple or type(value) ==list, "need a tuple or list for roi shape"
        assert value[0] >= 1024 or value[1] >= 1024, "ROI size cant exceed 1024"
        self._roi_shape = value
        
        AOI = self.thorcam.is_AOI
        AOI.argtypes = [ctypes.POINTER(ctypes.c_int)]
    @property
    def memory(self):
        return self._memory
    @memory.setter
    def memory(self,value=None):
        if value != None:
            self.thorcam.is_FreeImageMem(self.handle,self._memory[0],self._memory[1])
        xdim = self.roi_shape[0]
        ydim = self.roi_shape[1]
        image_size = xdim*ydim
        memory_id = ctypes.c_int(0)
        c_buf = (ctypes.c_ubyte * image_size)(0)
        self.thorcam.is_SetAllocatedImageMem(self.handle,xdim,ydim,8,c_buf, ctypes.byref(memory_id))
        self.thorcam.is_SetImageMem(self.handle,c_buf,ctypes.byref(memory_id))
        self._memory = [c_buf,memory_id]
    
    @property
    def exposure(self):
        return self._exposure
    @exposure.setter
    def exposure(self,value):
        self._exposure = ctypes.c_double(value)
        camera_exposure = self.thorcam.is_Exposure
        camera_exposure.argtypes = [ctypes.c_int,ctypes.c_uint,ctypes.POINTER(ctypes.c_double),ctypes.c_uint]
        camera_exposure(self.handle,12,self._exposure,self.bit_depth) # apparently 12 allows user to set exposure time
    
    @property
    def frame_rate(self):
        return self._frame_rate
    @frame_rate.setter
    def frame_rate(self,value):
        assert value <= 25, "maximum frame rate for camera is 25 frames per second"
        assert value > 0, "a frame rate of zero implies the camera isn't on like figure it out"
        self._frame_rate = value
        camera_frame_rate = self.thorcam.is_SetFrameRate
        camera_frame_rate.argtypes = [ctypes.c_int,ctypes.c_double,ctypes.POINTER(ctypes.c_double)]
        camera_frame_rate(self.handle,self._frame_rate,ctypes.byref(ctypes.c_double(0)))
    
    def get_image(self):
        im = np.frombuffer(self.memory[0], ctypes.c_ubyte).reshape(self.roi_shape[1], self.roi_shape[0])
        return im
        
    def show_image(self,figure):
        plt.figure(1); 
        plt.clf()
        plt.imshow(self.get_image())
        plt.draw()
        plt.pause(0.01)
    def image_clear(self,figure):
        figure.clear()
if __name__ == "__main__":
    mycam  = thorcam()
    mycam.start_video()
    value = True
    count = 0
    my_figure = plt.figure()
    while count < 100:
        #time.sleep(0.01)
        mycam.show_image(my_figure)
        #mycam.image_clear(my_figure)
        count +=1
    #input("press enter to end video")
    mycam.end_video()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
