# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apdWduzLj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
from datetime import date

sys.path.append(r"C:\Users\Goldsmith\Desktop\Hardware")
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from APD_Control.Thorlabs_APD import APD_Reader
from Miscellaneous.functionGenerator import FunctionGenerator
from FFPC_Programs.cavityCalculations import fittingCavityLength # this will be incorporated in the near future when we can actually work on cavity length scans
from FFPC_Programs.initialValues import initializeValues

from signalOutput import signalOutputDAQ#, workerOutput
from FFPC_Programs.cavityCalculations import QFactor
from TLB_6700.TLB_6700_control import TLB_6700_controller

import numpy as np
from statistics import mean
import pyqtgraph as pg
import pyvisa as visa
import pandas as pd
import time

class Ui_CavityLengthScan(object):
    """
    This is supposed to be the main program for measuring Q-factors, finesses, taking timed measurements and sending signals to the function generator

    simple way to run the program through powershell
    python ./CavityLengthScan.py

    
    """
    def __init__(self):
        # whenever you want to track a new value, add the name to the end of this list
        names = ['frequency','minVoltage','maxVoltage','amplitude','funcGenFrequency','phase','offset']
        self.values = initializeValues(names)
    def setupUi(self, CavityLengthScan):
        if not CavityLengthScan.objectName():
            CavityLengthScan.setObjectName(u"CavityLengthScan")
        CavityLengthScan.resize(1537, 701)
        self.centralwidget = QWidget(CavityLengthScan)
        self.centralwidget.setObjectName(u"centralwidget")
        self.apd_graph = pg.PlotWidget(self.centralwidget)
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(QRect(30, 270, 461, 361))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(220, 190, 131, 51))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(360, 190, 131, 51))
        self.stop.setFont(font)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(530, 550, 131, 31))
        self.frequency.setFont(font)
        self.frequency.setMaximum(10000.000000000000000)
        self.frequency.setSingleStep(0.100000000000000)
        self.frequency.setValue(10.000000000000000)
        self.labelFrequency = QLabel(self.centralwidget)
        self.labelFrequency.setObjectName(u"labelFrequency")
        self.labelFrequency.setGeometry(QRect(530, 520, 131, 31))
        self.labelFrequency.setFont(font)
        self.labelDaqList = QLabel(self.centralwidget)
        self.labelDaqList.setObjectName(u"labelDaqList")
        self.labelDaqList.setGeometry(QRect(530, 450, 131, 31))
        self.labelDaqList.setFont(font)
        self.daqList = QListWidget(self.centralwidget)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        QListWidgetItem(self.daqList)
        self.daqList.setObjectName(u"daqList")
        self.daqList.setGeometry(QRect(530, 480, 111, 31))
        self.daqList.setFont(font)
        self.daqList.setSortingEnabled(False)
        self.minVoltage = QDoubleSpinBox(self.centralwidget)
        self.minVoltage.setObjectName(u"minVoltage")
        self.minVoltage.setGeometry(QRect(530, 420, 131, 21))
        self.minVoltage.setFont(font)
        self.labelMinVoltage = QLabel(self.centralwidget)
        self.labelMinVoltage.setObjectName(u"labelMinVoltage")
        self.labelMinVoltage.setGeometry(QRect(530, 390, 161, 31))
        self.labelMinVoltage.setFont(font)
        self.labelMaxVoltage = QLabel(self.centralwidget)
        self.labelMaxVoltage.setObjectName(u"labelMaxVoltage")
        self.labelMaxVoltage.setGeometry(QRect(530, 340, 131, 31))
        self.labelMaxVoltage.setFont(font)
        self.maxVoltage = QDoubleSpinBox(self.centralwidget)
        self.maxVoltage.setObjectName(u"maxVoltage")
        self.maxVoltage.setGeometry(QRect(530, 370, 131, 21))
        self.maxVoltage.setFont(font)
        self.maxVoltage.setValue(10)
        self.cavityName = QPlainTextEdit(self.centralwidget)
        self.cavityName.setObjectName(u"cavityName")
        self.cavityName.setGeometry(QRect(220, 130, 291, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.cavityName.setFont(font1)
        self.labelFolderName = QLabel(self.centralwidget)
        self.labelFolderName.setObjectName(u"labelFolderName")
        self.labelFolderName.setGeometry(QRect(540, 100, 131, 16))
        self.labelFolderName.setFont(font1)
        self.labelComments = QLabel(self.centralwidget)
        self.labelComments.setObjectName(u"labelComments")
        self.labelComments.setGeometry(QRect(540, 180, 131, 16))
        self.labelComments.setFont(font1)
        self.labelCavityName = QLabel(self.centralwidget)
        self.labelCavityName.setObjectName(u"labelCavityName")
        self.labelCavityName.setGeometry(QRect(220, 100, 131, 16))
        self.labelCavityName.setFont(font1)
        self.labelWhoAreYou = QLabel(self.centralwidget)
        self.labelWhoAreYou.setObjectName(u"labelWhoAreYou")
        self.labelWhoAreYou.setGeometry(QRect(30, 100, 121, 21))
        self.labelWhoAreYou.setFont(font1)
        self.comments = QPlainTextEdit(self.centralwidget)
        self.comments.setObjectName(u"comments")
        self.comments.setGeometry(QRect(540, 210, 331, 41))
        self.comments.setFont(font1)
        self.whoAreYou = QListWidget(self.centralwidget)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        self.whoAreYou.setObjectName(u"whoAreYou")
        self.whoAreYou.setGeometry(QRect(30, 130, 171, 41))
        self.whoAreYou.setFont(font1)
        self.labelFileLocationPath = QLabel(self.centralwidget)
        self.labelFileLocationPath.setObjectName(u"labelFileLocationPath")
        self.labelFileLocationPath.setGeometry(QRect(30, 10, 231, 16))
        self.labelFileLocationPath.setFont(font1)
        self.localOrDatabackup = QCheckBox(self.centralwidget)
        self.localOrDatabackup.setObjectName(u"localOrDatabackup")
        self.localOrDatabackup.setGeometry(QRect(30, 200, 241, 31))
        self.localOrDatabackup.setFont(font1)
        self.folderName = QPlainTextEdit(self.centralwidget)
        self.folderName.setObjectName(u"folderName")
        self.folderName.setGeometry(QRect(540, 130, 331, 41))
        self.folderName.setFont(font1)
        self.fileLocationPath = QPlainTextEdit(self.centralwidget)
        self.fileLocationPath.setObjectName(u"fileLocationPath")
        self.fileLocationPath.setGeometry(QRect(30, 40, 841, 41))
        self.fileLocationPath.setFont(font1)
        self.save = QPushButton(self.centralwidget)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(740, 580, 131, 51))
        self.save.setFont(font)
        self.amplitude = QDoubleSpinBox(self.centralwidget)
        self.amplitude.setObjectName(u"amplitude")
        self.amplitude.setGeometry(QRect(740, 370, 131, 21))
        self.amplitude.setFont(font)
        self.amplitude.setKeyboardTracking(False)
        self.labelAPDControls = QLabel(self.centralwidget)
        self.labelAPDControls.setObjectName(u"labelAPDControls")
        self.labelAPDControls.setGeometry(QRect(530, 310, 101, 31))
        self.labelAPDControls.setFont(font)
        self.labelFuncGenControls = QLabel(self.centralwidget)
        self.labelFuncGenControls.setObjectName(u"labelFuncGenControls")
        self.labelFuncGenControls.setGeometry(QRect(740, 250, 141, 41))
        self.labelFuncGenControls.setFont(font)
        self.labelAmplitude = QLabel(self.centralwidget)
        self.labelAmplitude.setObjectName(u"labelAmplitude")
        self.labelAmplitude.setGeometry(QRect(740, 340, 101, 31))
        self.labelAmplitude.setFont(font)
        self.funcGenFrequency = QDoubleSpinBox(self.centralwidget)
        self.funcGenFrequency.setObjectName(u"funcGenFrequency")
        self.funcGenFrequency.setGeometry(QRect(740, 420, 131, 21))
        self.funcGenFrequency.setFont(font)
        self.funcGenFrequency.setKeyboardTracking(False)
        self.labelFuncGenFrequency = QLabel(self.centralwidget)
        self.labelFuncGenFrequency.setObjectName(u"labelFuncGenFrequency")
        self.labelFuncGenFrequency.setGeometry(QRect(740, 390, 101, 31))
        self.labelFuncGenFrequency.setFont(font)
        self.offset = QDoubleSpinBox(self.centralwidget)
        self.offset.setObjectName(u"offset")
        self.offset.setGeometry(QRect(740, 480, 131, 21))
        self.offset.setFont(font)
        self.offset.setDecimals(4)
        self.offset.setSingleStep(0.001000000)
        self.offset.setKeyboardTracking(False)
        #self.offset.setValue(0.2000)
        self.labelOffset = QLabel(self.centralwidget)
        self.labelOffset.setObjectName(u"labelOffset")
        self.labelOffset.setGeometry(QRect(740, 450, 101, 31))
        self.labelOffset.setFont(font)
        self.phase = QDoubleSpinBox(self.centralwidget)
        self.phase.setObjectName(u"phase")
        self.phase.setGeometry(QRect(740, 540, 131, 21))
        self.phase.setFont(font)
        self.phase.setMaximum(360)
        self.phase.setValue(270.0)
        self.labelPhase = QLabel(self.centralwidget)
        self.labelPhase.setObjectName(u"labelPhase")
        self.labelPhase.setGeometry(QRect(740, 510, 101, 31))
        self.labelPhase.setFont(font)
        self.funcGenSwitch = QCheckBox(self.centralwidget)
        self.funcGenSwitch.setObjectName(u"funcGenSwitch")
        self.funcGenSwitch.setGeometry(QRect(700, 310, 171, 21))
        self.funcGenSwitch.setFont(font)
        self.funcGenSwitch.setFont(font)
        self.scanSwitch = QCheckBox(self.centralwidget)
        self.scanSwitch.setObjectName(u"scanSwitch")
        self.scanSwitch.setGeometry(QRect(700, 280, 171, 31))
        self.scanSwitch.setFont(font)
        self.timedOrContinuous = QCheckBox(self.centralwidget)
        self.timedOrContinuous.setObjectName(u"timedOrContinuous")
        self.timedOrContinuous.setGeometry(QRect(900, 350, 211, 61))
        self.timedOrContinuous.setFont(font)
        self.labelLengthOfMeasurement = QLabel(self.centralwidget)
        self.labelLengthOfMeasurement.setObjectName(u"labelLengthOfMeasurement")
        self.labelLengthOfMeasurement.setGeometry(QRect(900, 410, 241, 21))
        self.labelLengthOfMeasurement.setFont(font)
        self.lengthOfMeasurement = QSpinBox(self.centralwidget)
        self.lengthOfMeasurement.setObjectName(u"lengthOfMeasurement")
        self.lengthOfMeasurement.setGeometry(QRect(900, 440, 101, 22))
        self.lengthOfMeasurement.setFont(font)
        self.lengthOfMeasurement.setMaximum(100000)
        self.lengthOfMeasurement.setValue(100)
        self.QFactorOrFinesse = QCheckBox(self.centralwidget)
        self.QFactorOrFinesse.setObjectName(u"QFactorOrFinesse")
        self.QFactorOrFinesse.setGeometry(QRect(900, 480, 241, 51))
        self.QFactorOrFinesse.setFont(font)
        self.valueFinesse = QLCDNumber(self.centralwidget)
        self.valueFinesse.setObjectName(u"valueFinesse")
        self.valueFinesse.setGeometry(QRect(900, 590, 201, 31))
        self.valueFinesse.setFont(font)
        self.valueFinesse.setDigitCount(8)
        self.valueFinesse.setSmallDecimalPoint(False)
        self.valueFinesse.setProperty("value", 0.000000000000000)
        self.calculateFinesse = QPushButton(self.centralwidget)
        self.calculateFinesse.setObjectName(u"calculateFinesse")
        self.calculateFinesse.setGeometry(QRect(900, 530, 171, 41))
        self.calculateFinesse.setFont(font)
        
        self.labelLaserConditions = QLabel(self.centralwidget)
        self.labelLaserConditions.setObjectName(u"labelLaserConditions")
        self.labelLaserConditions.setGeometry(QRect(910, 40, 141, 16))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.labelLaserConditions.setFont(font2)
        self.controlLaser = QCheckBox(self.centralwidget)
        self.controlLaser.setObjectName(u"controlLaser")
        self.controlLaser.setEnabled(True)
        self.controlLaser.setGeometry(QRect(910, 70, 121, 31))
        self.controlLaser.setFont(font)
        self.controlLaser.setChecked(False)
        self.laserStatus = QCheckBox(self.centralwidget)
        self.laserStatus.setObjectName(u"laserStatus")
        self.laserStatus.setGeometry(QRect(910, 110, 101, 16))
        self.laserStatus.setFont(font)
        self.startWavelengthScan = QPushButton(self.centralwidget)
        self.startWavelengthScan.setObjectName(u"startWavelengthScan")
        self.startWavelengthScan.setGeometry(QRect(1110, 80, 181, 31))
        self.startWavelengthScan.setFont(font)
        self.stopWavelengthScan = QPushButton(self.centralwidget)
        self.stopWavelengthScan.setObjectName(u"stopWavelengthScan")
        self.stopWavelengthScan.setGeometry(QRect(1310, 80, 181, 31))
        self.stopWavelengthScan.setFont(font)
        self.displayWavelength = QLCDNumber(self.centralwidget)
        self.displayWavelength.setObjectName(u"displayWavelength")
        self.displayWavelength.setGeometry(QRect(910, 274, 141, 31))
        self.displayWavelength.setDigitCount(9)
        self.labelWavelengthDisplay = QLabel(self.centralwidget)
        self.labelWavelengthDisplay.setObjectName(u"labelWavelengthDisplay")
        self.labelWavelengthDisplay.setGeometry(QRect(910, 250, 121, 20))
        self.labelWavelengthDisplay.setFont(font)
        self.displayCurrent = QLCDNumber(self.centralwidget)
        self.displayCurrent.setObjectName(u"displayCurrent")
        self.displayCurrent.setGeometry(QRect(910, 330, 141, 31))
        self.labelDisplayCurrent = QLabel(self.centralwidget)
        self.labelDisplayCurrent.setObjectName(u"labelDisplayCurrent")
        self.labelDisplayCurrent.setGeometry(QRect(910, 310, 121, 20))
        self.labelDisplayCurrent.setFont(font)
        self.labelDisplayPower = QLabel(self.centralwidget)
        self.labelDisplayPower.setObjectName(u"labelDisplayPower")
        self.labelDisplayPower.setGeometry(QRect(1080, 310, 121, 20))
        self.labelDisplayPower.setFont(font)
        self.displayPower = QLCDNumber(self.centralwidget)
        self.displayPower.setObjectName(u"displayPower")
        self.displayPower.setGeometry(QRect(1080, 330, 141, 31))
        self.setWavelength = QDoubleSpinBox(self.centralwidget)
        self.setWavelength.setObjectName(u"setWavelength")
        self.setWavelength.setGeometry(QRect(910, 210, 141, 31))
        self.setWavelength.setFont(font)
        self.setWavelength.setMinimum(765.000000000000000)
        self.setWavelength.setMaximum(781.000000000000000)
        self.setWavelength.setSingleStep(0.010000000000000)
        self.setWavelength.setKeyboardTracking(False)
        self.labelSetWavelength = QLabel(self.centralwidget)
        self.labelSetWavelength.setObjectName(u"labelSetWavelength")
        self.labelSetWavelength.setGeometry(QRect(910, 180, 161, 20))
        self.labelSetWavelength.setFont(font)
        self.setCurrentPower = QDoubleSpinBox(self.centralwidget)
        self.setCurrentPower.setObjectName(u"setCurrentPower")
        self.setCurrentPower.setGeometry(QRect(1080, 270, 141, 31))
        self.setCurrentPower.setFont(font)
        self.setCurrentPower.setMaximum(200.000000000000000)
        self.setCurrentPower.setKeyboardTracking(False)
        self.labelSetCurrentPower = QLabel(self.centralwidget)
        self.labelSetCurrentPower.setObjectName(u"labelSetCurrentPower")
        self.labelSetCurrentPower.setGeometry(QRect(1080, 240, 211, 20))
        self.labelSetCurrentPower.setFont(font)
        self.powerOrCurrent = QCheckBox(self.centralwidget)
        self.powerOrCurrent.setObjectName(u"powerOrCurrent")
        self.powerOrCurrent.setGeometry(QRect(1080, 210, 181, 17))
        self.powerOrCurrent.setFont(font)
        self.powerOrCurrent.setChecked(True)
        self.setStartWavelengthScan = QDoubleSpinBox(self.centralwidget)
        self.setStartWavelengthScan.setObjectName(u"startWavelengthScan_2")
        self.setStartWavelengthScan.setGeometry(QRect(1210, 120, 81, 22))
        self.setStartWavelengthScan.setFont(font)
        self.setStartWavelengthScan.setMinimum(765.000000000000000)
        self.setStartWavelengthScan.setMaximum(780.990000000000009)
        self.setStartWavelengthScan.setKeyboardTracking(False)
        self.setEndWavelengthScan = QDoubleSpinBox(self.centralwidget)
        self.setEndWavelengthScan.setObjectName(u"endWavelengthScan")
        self.setEndWavelengthScan.setGeometry(QRect(1210, 150, 81, 22))
        self.setEndWavelengthScan.setFont(font)
        self.setEndWavelengthScan.setMinimum(765.009999999999991)
        self.setEndWavelengthScan.setMaximum(781.000000000000000)
        self.setEndWavelengthScan.setValue(781.00)
        self.setEndWavelengthScan.setKeyboardTracking(False)
        self.scanSpeed = QDoubleSpinBox(self.centralwidget)
        self.scanSpeed.setObjectName(u"scanSpeed")
        self.scanSpeed.setGeometry(QRect(1440, 150, 81, 22))
        self.scanSpeed.setFont(font)
        self.scanSpeed.setMinimum(0.010000000000000)
        self.scanSpeed.setMaximum(8.000000000000000)
        self.scanSpeed.setSingleStep(0.010000000000000)
        self.scanSpeed.setValue(0.100000000000000)
        self.scanSpeed.setKeyboardTracking(False)
        self.labelStartWavelength = QLabel(self.centralwidget)
        self.labelStartWavelength.setObjectName(u"labelStartWavelength")
        self.labelStartWavelength.setGeometry(QRect(1030, 120, 171, 21))
        self.labelStartWavelength.setFont(font)
        self.labelStartWavelength.setLayoutDirection(Qt.LeftToRight)
        self.labelStartWavelength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelStartWavelength.setWordWrap(False)
        self.labelEndWavelength = QLabel(self.centralwidget)
        self.labelEndWavelength.setObjectName(u"labelEndWavelength")
        self.labelEndWavelength.setGeometry(QRect(1030, 150, 171, 21))
        self.labelEndWavelength.setFont(font)
        self.labelEndWavelength.setLayoutDirection(Qt.LeftToRight)
        self.labelEndWavelength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelEndWavelength.setWordWrap(False)
        self.labelScanSpeed = QLabel(self.centralwidget)
        self.labelScanSpeed.setObjectName(u"labelScanSpeed")
        self.labelScanSpeed.setGeometry(QRect(1260, 150, 171, 21))
        self.labelScanSpeed.setFont(font)
        self.labelScanSpeed.setLayoutDirection(Qt.LeftToRight)
        self.labelScanSpeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelScanSpeed.setWordWrap(False)
        self.numberOfScans = QSpinBox(self.centralwidget)
        self.numberOfScans.setObjectName(u"numberOfScans")
        self.numberOfScans.setGeometry(QRect(1440, 120, 81, 22))
        self.numberOfScans.setFont(font)
        self.numberOfScans.setMinimum(1)
        self.numberOfScans.setMaximum(1000)
        self.labelNumberOfScans = QLabel(self.centralwidget)
        self.labelNumberOfScans.setObjectName(u"labelNumberOfScans")
        self.labelNumberOfScans.setGeometry(QRect(1290, 120, 141, 20))
        self.labelNumberOfScans.setFont(font)
        self.labelNumberOfScans.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        CavityLengthScan.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CavityLengthScan)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 908, 21))
        CavityLengthScan.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CavityLengthScan)
        self.statusbar.setObjectName(u"statusbar")
        CavityLengthScan.setStatusBar(self.statusbar)

        self.retranslateUi(CavityLengthScan)

        self.daqList.setCurrentRow(-1)

        # keep all of the set values here, if there are more values you want to track feel free to add those here following the same
        # outline that is shown below
        self.scanSwitch.setChecked(True)
        self.amplitude.setValue(self.values.getEntry("amplitude"))
        self.funcGenFrequency.setValue(self.values.getEntry("funcGenFrequency"))
        self.phase.setValue(self.values.getEntry("phase"))
        self.offset.setValue(self.values.getEntry("offset"))
        self.frequency.setValue(self.values.getEntry("frequency"))
        self.maxVoltage.setValue(self.values.getEntry("maxVoltage"))
        self.minVoltage.setValue(self.values.getEntry("minVoltage"))
        self.resolution = 1000000 # this value is the fastest the daq can read values at, lower will decrease the data points collected but higher will just not work
        QMetaObject.connectSlotsByName(CavityLengthScan)
        #all of the rest of the code that I have added is below
        #If any changes are made to the ui, copy everything down
        #and only replace components above the top most comment
        #and replace the retranslateUI function.
        self._today = date.today()
        self._traceNum = 0
        # the function generator code i have written, this is suboptimal as I have hard coded the USB address of the instrument
        # I am thinking of ways of improving this in the future but for now we are stuck, my idea is to do a query of all the instruments to determine what they are
        # and then match them to an instrument that we desire by using regular expressions, not totally optimal but better than current approach as we can only currently
        # use the exact rigol we currently have
        self.daqOutput = True #I will add a check box for this later if I have to
        if not self.daqOutput:
            self._rm = visa.ResourceManager()
            try:
                self._resource = self._rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD212800749::INSTR',timeout=1)
                self._func_gen = FunctionGenerator(self._resource,"SOUR1")
            except visa.errors.VisaIOError:
                raise ValueError("Make sure the function generator is turned on")
        self.laser = None
        self.connect_to_laser()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._timer = None
        self._apd = None
        self._active = False
        self._values = None

        #for timed channel
        self.timedList = []
        self.timedValues = []
        self.currentTime = 0
        self.wavelengthList = []
        self.currentScan = 1
        self.wavelengthScan = False
        
        #self.frequency.valueChanged.connect(self.change_value)
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        self.daqList.currentItemChanged.connect(self.change_value)
        self.maxVoltage.valueChanged.connect(self.change_value)
        self.minVoltage.valueChanged.connect(self.change_value)
        self.funcGenSwitch.stateChanged.connect(self.func_generation)
        self.scanSwitch.stateChanged.connect(self.func_generation)
        self.funcGenFrequency.valueChanged.connect(self.func_generation)
        self.amplitude.valueChanged.connect(self.func_generation)
        self.phase.valueChanged.connect(self.func_generation)
        self.offset.valueChanged.connect(self.func_generation)
        self.save.clicked.connect(self.save_values)
        self.calculateFinesse.clicked.connect(self.qFactor_or_finesse)
        
        self.controlLaser.stateChanged.connect(self.connect_to_laser)
        self.laserStatus.stateChanged.connect(self.change_laser_state)
        self.setWavelength.valueChanged.connect(self.change_laser_wavelength)
        self.startWavelengthScan.clicked.connect(self.start_scan)
        self.stopWavelengthScan.clicked.connect(self.stop_scan)
        self.setStartWavelengthScan.valueChanged.connect(self.change_start_scan_wavelength)
        self.setEndWavelengthScan.valueChanged.connect(self.change_end_scan_wavelength)
        self.setCurrentPower.valueChanged.connect(self.change_laser_power_or_current)
        self.powerOrCurrent.stateChanged.connect(self.switch_between_power_current)
        self.numberOfScans.valueChanged.connect(self.change_number_scans)
        self.scanSpeed.valueChanged.connect(self.change_velocity_scan)
        
    def retranslateUi(self, apdMonitor):
        CavityLengthScan.setWindowTitle(QCoreApplication.translate("CavityLengthScan", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("CavityLengthScan", u"Start", None))
        self.stop.setText(QCoreApplication.translate("CavityLengthScan", u"Stop", None))
        self.labelFrequency.setText(QCoreApplication.translate("CavityLengthScan", u"Frequency", None))
        self.labelDaqList.setText(QCoreApplication.translate("CavityLengthScan", u"DAQ Channel", None))

        __sortingEnabled = self.daqList.isSortingEnabled()
        self.daqList.setSortingEnabled(False)
        ___qlistwidgetitem = self.daqList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai0", None));
        ___qlistwidgetitem1 = self.daqList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai1", None));
        ___qlistwidgetitem2 = self.daqList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai2", None));
        ___qlistwidgetitem3 = self.daqList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai3", None));
        ___qlistwidgetitem4 = self.daqList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai4", None));
        ___qlistwidgetitem5 = self.daqList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai5", None));
        ___qlistwidgetitem6 = self.daqList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai6", None));
        ___qlistwidgetitem7 = self.daqList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("CavityLengthScan", u"Dev1/ai7", None));
        self.daqList.setSortingEnabled(__sortingEnabled)

        self.labelMinVoltage.setText(QCoreApplication.translate("CavityLengthScan", u"Minimum Voltage", None))
        self.labelMaxVoltage.setText(QCoreApplication.translate("CavityLengthScan", u"Maximum Voltage", None))
        self.cavityName.setPlainText(QCoreApplication.translate("CavityLengthScan", u"Cavity", None))
        self.labelFolderName.setText(QCoreApplication.translate("CavityLengthScan", u"Folder Name?", None))
        self.labelComments.setText(QCoreApplication.translate("CavityLengthScan", u"Comments?", None))
        self.labelCavityName.setText(QCoreApplication.translate("CavityLengthScan", u"Cavity Name?", None))
        self.labelWhoAreYou.setText(QCoreApplication.translate("CavityLengthScan", u"Who Are you?", None))
        self.comments.setPlainText("")

        __sortingEnabled1 = self.whoAreYou.isSortingEnabled()
        self.whoAreYou.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.whoAreYou.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("CavityLengthScan", u"Brandon Mehlenbacher", None));
        ___qlistwidgetitem10 = self.whoAreYou.item(1)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("CavityLengthScan", u"Lisa-Maria", None));
        ___qlistwidgetitem11 = self.whoAreYou.item(2)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("CavityLengthScan", u"Beau", None));
        ___qlistwidgetitem12 = self.whoAreYou.item(3)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("CavityLengthScan", u"Ceci", None));
        ___qlistwidgetitem13 = self.whoAreYou.item(4)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("CavityLengthScan", u"Julia", None));
        self.whoAreYou.setSortingEnabled(__sortingEnabled1)

        self.labelFileLocationPath.setText(QCoreApplication.translate("CavityLengthScan", u"File Location Path", None))
        self.localOrDatabackup.setText(QCoreApplication.translate("CavityLengthScan", u"Local (T) / Databackup (F)", None))
        self.folderName.setPlainText(QCoreApplication.translate("CavityLengthScan", u"Cavity", None))
        self.save.setText(QCoreApplication.translate("CavityLengthScan", u"Save", None))
        self.labelAPDControls.setText(QCoreApplication.translate("CavityLengthScan", u"APD Controls", None))
        self.labelFuncGenControls.setText(QCoreApplication.translate("CavityLengthScan", u"Func Gen Controls", None))
        self.labelAmplitude.setText(QCoreApplication.translate("CavityLengthScan", u"Amplitude", None))
        self.labelFuncGenFrequency.setText(QCoreApplication.translate("CavityLengthScan", u"Frequency", None))
        self.labelOffset.setText(QCoreApplication.translate("CavityLengthScan", u"Offset", None))
        self.labelPhase.setText(QCoreApplication.translate("CavityLengthScan", u"Phase", None))
        self.funcGenSwitch.setText(QCoreApplication.translate("CavityLengthScan", u"Function Gen Switch", None))
        self.scanSwitch.setText(QCoreApplication.translate("CavityLengthScan", u"Scan/No Scan", None))
        self.timedOrContinuous.setText(QCoreApplication.translate("CavityLengthScan", u"Timed(T)/Continuous(F)", None))
        self.labelLengthOfMeasurement.setText(QCoreApplication.translate("CavityLengthScan", u"Length of Measurement time (s)", None))
        self.QFactorOrFinesse.setText(QCoreApplication.translate("CavityLengthScan", u"Quality Factor (T)/Finesse (F)", None))
        self.calculateFinesse.setText(QCoreApplication.translate("CavityLengthScan", u"Calculate Q/Finesse", None))
        self.labelLaserConditions.setText(QCoreApplication.translate("CavityLengthScan", u"Laser Conditions", None))
        self.controlLaser.setText(QCoreApplication.translate("CavityLengthScan", u"Control Laser", None))
        self.laserStatus.setText(QCoreApplication.translate("CavityLengthScan", u"ON/OFF", None))
        self.startWavelengthScan.setText(QCoreApplication.translate("CavityLengthScan", u"Start Wavelength Scan", None))
        self.stopWavelengthScan.setText(QCoreApplication.translate("CavityLengthScan", u"Stop Wavelength Scan", None))
        self.labelWavelengthDisplay.setText(QCoreApplication.translate("CavityLengthScan", u"Wavelength (nm)", None))
        self.labelDisplayCurrent.setText(QCoreApplication.translate("CavityLengthScan", u"Current (mA)", None))
        self.labelDisplayPower.setText(QCoreApplication.translate("CavityLengthScan", u"Power (mW)", None))
        self.labelSetWavelength.setText(QCoreApplication.translate("CavityLengthScan", u"Set Wavelength", None))
        self.labelSetCurrentPower.setText(QCoreApplication.translate("CavityLengthScan", u"Set Current/Power (mA/mW)", None))
        self.powerOrCurrent.setText(QCoreApplication.translate("CavityLengthScan", u"Power(T)/Current(F)", None))
        self.labelStartWavelength.setText(QCoreApplication.translate("CavityLengthScan", u"Start Wavelength (nm)", None))
        self.labelEndWavelength.setText(QCoreApplication.translate("CavityLengthScan", u"End Wavelength (nm)", None))
        self.labelScanSpeed.setText(QCoreApplication.translate("CavityLengthScan", u"Scan Speed (nm/s)", None))
        self.labelNumberOfScans.setText(QCoreApplication.translate("CavityLengthScan", u"Number Of Scans", None))
        
    #function for starting the acquisition 
    def start_acq(self):
        print(self.daqList.currentItem().text())
        #in case we want to use the DAQ as the output, needs work before it will be able to be implemented, currently gets stuck in an infinite loop
        self.output = signalOutputDAQ("Dev1/ao0", 1000000,frequency = self.funcGenFrequency.value(),amplitude = self.amplitude.value(),offset=self.offset.value())
        #self.worker =  workerOutput(self.output)
        #self.worker.start()
        self._timer = QTimer()
        time = (1/self.frequency.value())*1000
        self._apd = APD_Reader(self.daqList.currentItem().text(),int(self.resolution/(self.frequency.value())),max_val = self.maxVoltage.value(),min_val = self.minVoltage.value(),continuous = False)
        self._apd.start_acquisition()
        self.output.start_acq()
        self._timer.start(time)
        self._timer.timeout.connect(self.graph_values)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self._active = True
    #function for stopping the acquisition
    def stop_acq(self):
        #self.worker.terminateLoop()
        #self.worker.quit()
        self._timer.stop()
        self._apd.stop_acquisition()
        self.output.stop_acq()
        self._apd.close_daq()
        self.output.close_daq()
        
        self._apd = None
        self.output = None
        #self._timer.stop()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._active = False
    #if any of the values have changed, everything gets reset if the DAQ is actually active, if not ignores it
    def change_value(self):
        self.saveNewValues()
        if self._active:
            self._apd.stop_acquisition()
            self._apd.close_daq()
            self._apd = None
            self._apd = APD_Reader(self.daqList.currentItem().text(),int(self.resolution/(self.frequency.value())),max_val = self.maxVoltage.value(),min_val = self.minVoltage.value(),continuous = False)
            self._apd.start_acquisition()
            time = (1/self.frequency.value())*1000
            self._timer.start(time)
            self._timer.timeout.connect(self.graph_values)
            
    #plots all of the values from the APD in the pyqtplot
    def graph_values(self):
        """
        This is used for graphing the values on the apd_graph as well as read the values off of the APD

        Inputs: (Although technically no inputs there are several worth mentioning even though they are embedded in the gui)
        self.apd_graph: the pyqtgraph we are using in the gui or a matplotlib figure object will also work
        self._apd: the daq board channel we are reading off from, we consider this the apd because that is where we are generally getting our signal from
        self.timedOrContinuous: a QCheckbox object that determines if we are measuring it over time or not

        Outputs:
        a graph with all of the data
        """
        self.apd_graph.clear()
        self._values = self._apd.read_values()
        self._apd.stop_acquisition()
        self._apd.start_acquisition()

        if self.timedOrContinuous.isChecked():
            if not self.wavelengthScan:
                self.currentTime += 1/self.frequency.value()
                self.timedList.append(self.currentTime)
            else:
                self.timedList.append(self.laser.get_wavelength())
                self.displayWavelength.display(self.laser.get_wavelength())
            self.timedValues.append(sum(self._values)/len(self._values))
            self.apd_graph.plot(self.timedList,self.timedValues)
            if self.wavelengthScan:
                
                if self.laser.get_actual_number_scans() == self.numberOfScans.value():
                    #self.stop_scan()
                    self.save_values()
                    self.timedOrContinuous.setChecked(False)
                    self.timedOrContinuous.setEnabled(True)
                    self.timedList = []
                    self.timedValues = []
                    self.currentScan=1
                elif self.currentScan == self.laser.get_actual_number_scans():
                    self.save_values()
                    self.timedList = []
                    self.timedValues = []
                    self.currentScan+=1

            elif self.currentTime >= self.lengthOfMeasurement.value():
                self.save_values()
                self.timedOrContinuous.setChecked(False)
                self.timedList = []
                self.timedValues = []
        else:
            self.apd_graph.plot(self._values)
            self.timedList = []
            self.timedValues = []
            self.currentTime = 0
            
    def save_values(self):
        self._traceNum+=1;
        stopped = False
        if self._active:
            self.stop_acq()
            stopped = True
        if self.localOrDatabackup.isChecked():
            current_directory = os.getcwd()
            directory = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()
            self._filename = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()+f"_{self._traceNum}.csv"
            self.fileLocationPath.setPlainText(self._filename)
        else:
            current_directory = "//marlin.chem.wisc.edu/Groups/Goldsmith Group/X/dataBackup/ELN_Data"
            directory = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()
            self._filename = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()+f"_{self._traceNum}.csv"
            self.fileLocationPath.setPlainText(self._filename)
        if self.timedOrContinuous.isChecked():
            saveValues = np.transpose(np.array([self.timedList,self.timedValues],ndmin=2))
        else:
            saveValues = np.array(self._values)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        np.savetxt(self._filename,saveValues,delimiter=',')
        if stopped:
            self.start_acq()
            
    def func_generation(self):
        self.saveNewValues()
        if not self.daqOutput:
            if self.funcGenSwitch.isChecked():
                if self.scanSwitch.isChecked():
                    self._func_gen.write_many(['FUNC:SHAP RAMP','VOLT:UNIT VPP',f"FREQ {self.funcGenFrequency.value()}",f"VOLT {self.amplitude.value()}",f"VOLT:OFFS {self.offset.value()}",f"PHAS {self.phase.value()}",'FUNC:RAMP:SYMM 50'])
                else:
                    self._func_gen.write_many(['FUNC:SHAP DC','VOLT:UNIT VPP',f"VOLT:OFFS {self.offset.value()}"])
                self._func_gen.write_many(['OUTP ON'])
            else:
                self._func_gen.write_many(['OUTP OFF'])
        else:
            self.output.stop_acq()
            self.output.close_daq()
            self.output = signalOutputDAQ("Dev1/ao0", 1000000,frequency = self.funcGenFrequency.value(),amplitude = self.amplitude.value(),offset=self.offset.value())
            self.output.start_acq()
            
    def saveNewValues(self):
        listValues = [self.frequency.value(),
                      self.minVoltage.value(),
                      self.maxVoltage.value(),
                      self.amplitude.value(),
                      self.funcGenFrequency.value(),
                      self.phase.value(),
                      self.offset.value(),
                      ]
        self.values.saveValues(listValues)
    def qFactor(self):
        if self._active:
            correction = int(1000000/self.funcGenFrequency.value())
            originalXValues = (120.5/correction)*np.array(range(correction))
            #self.apd_graph.clear()
            #self._values = self._apd.read_values()
            x_values = originalXValues[0:int(len(originalXValues)/2)]
            y_values = self._values[0:int(len(originalXValues)/2)]
            dataframe = pd.DataFrame({'x_values': x_values, 'y_values': y_values})
            self.apd_graph.plot(x_values, y_values)
            QCalc = QFactor(x_values, y_values)
            QCalc.fitLorentz()
            sigma = QCalc.getSigma()
            self.valueFinesse.display(780000/sigma)  # roughly the wavelength in picometers
            #newYValues = QCalc.getNewYVal()
           #self.apd_graph.plot(x_values, newYValues)
            #dataframe.to_csv(self._filename)
            #self.change_filename()
            #self._traceNum+=1;
            
    def qFactor_or_finesse(self):
        if self.QFactorOrFinesse.isChecked():
            self.qFactor()
        else:
            pass

    def connect_to_laser(self):
        if self.controlLaser.isChecked():
            self.laser = TLB_6700_controller("SN41044")
            self.displayWavelength.display(self.laser.get_wavelength())
            self.switch_between_power_current()
        else:
            if self.laser != None:
                self.laser.close_devices()

    def switch_between_power_current(self):
        if self.laser.get_output_state_laser():
            self.laser.output_state_laser(0)
            self.laserStatus.setChecked(False)
        if self.powerOrCurrent.isChecked():
            self.laser.change_mode_laser_power(1)
            self.displayPower.display(self.laser.get_power_diode())
            self.displayCurrent.display(0)
        else:
            self.laser.change_mode_laser_power(0)
            self.displayCurrent.display(self.laser.get_current_diode())
            self.displayPower.display(0)
            
    def change_laser_power_or_current(self):
        if self.powerOrCurrent.isChecked():
            self.laser.change_laser_power(self.setCurrentPower.value())
            time.sleep(2)
            self.displayPower.display(self.laser.get_power_diode())
        else:
            self.laser.change_laser_current(self.setCurrentPower.value())
            self.displayCurrent.display(self.laser.get_current_diode())
    
    def change_laser_state(self):
        if self.laserStatus.isChecked():
            self.laser.output_state_laser(1)
            time.sleep(2)
        else:
            self.laser.output_state_laser(0)
            time.sleep(0.1)

    def change_laser_wavelength(self):
        #if self.laser.operation_completed():
        if not self.wavelengthScan:
            if not self.laser.check_lambda_track():
                self.laser.change_state_lambda_track_on()
            self.laser.change_wavelength(self.setWavelength.value())
            self.displayWavelength.display(self.laser.get_wavelength())
            time.sleep(0.1)
        
    def change_number_scans(self):
        self.laser.change_number_scans(self.numberOfScans.value())
        time.sleep(0.1)
        
    def change_start_scan_wavelength(self):
        self.laser.change_start_scan_wavelength(self.setStartWavelengthScan.value())
        time.sleep(0.1)

    def change_velocity_scan(self):
        self.laser.change_velocity_wavelength_change_forward(self.scanSpeed.value())
        self.laser.change_velocity_wavelength_change_reverse(self.scanSpeed.value())
        time.sleep(0.1)
        
    def change_end_scan_wavelength(self):
        self.laser.change_end_scan_wavelength(self.setEndWavelengthScan.value())
        time.sleep(0.1)
        
    def start_scan(self):
        self.timedList = []
        self.timedValues = []
        self._timer.setInterval(300)
        self.laser.change_state_lambda_track_on()
        self.timedOrContinuous.setChecked(True)
        self.timedOrContinuous.setEnabled(False)
        self.wavelengthScan = True
        self.laser.start_scan()

    def stop_scan(self):
        self.timedList = []
        self.timedValues = []
        self.currentScan=1
        time = (1/self.frequency.value())*1000
        self._timer.setInterval(time)
        self.timedOrContinuous.setEnabled(True)
        self.wavelengthScan = False
        self.laser.end_scan()
        
#Feel free to copy and paste the line below in other GUIs you make, just make sure to change names within it
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    CavityLengthScan = QMainWindow()
    ui = Ui_CavityLengthScan()
    ui.setupUi(CavityLengthScan)
    CavityLengthScan.show()
    sys.exit(app.exec_())
    
