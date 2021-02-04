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
from cavityCalculations import fittingCavityLength # this will be incorporated in the near future when we can actually work on cavity length scans
from FFPC_Programs.initialValues import initializeValues
from signalOutput import signalOutput, workerOutput


import numpy as np
from statistics import mean
import pyqtgraph as pg
import pyvisa as visa


class Ui_CavityLengthScan(object):
    """
    The whole point of this gui is to simply monitor data gathered from and APD
    
    simple description of how to run this program
    
    Exec: python ./apd.py from the command line or powershell to initialize the program

    Run: Click the start button to begin acquisition. If no daq channel is specified it will prompt you to do so before it attempts to
    open the GUI. After it is open, the frequency, board input channel, and the max and min voltage can all be changed while running the program
    To stop data acquisition, simply hit the stop button and it will terminate
self.apd_graph = pg.PlotWidget(self.centralwidget)
    """
    def __init__(self):
        names = ['frequency','minVoltage','maxVoltage','amplitude','funcGenFrequency','phase','offset']
        self.values = initializeValues(names)
    def setupUi(self, CavityLengthScan):
        if not CavityLengthScan.objectName():
            CavityLengthScan.setObjectName(u"CavityLengthScan")
        CavityLengthScan.resize(1178, 701)
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

        #keep all of the set values here
        self.scanSwitch.setChecked(True)
        self.amplitude.setValue(self.values.getEntry("amplitude"))
        self.funcGenFrequency.setValue(self.values.getEntry("funcGenFrequency"))
        self.phase.setValue(self.values.getEntry("phase"))
        self.offset.setValue(self.values.getEntry("offset"))
        self.frequency.setValue(self.values.getEntry("frequency"))
        self.maxVoltage.setValue(self.values.getEntry("maxVoltage"))
        self.minVoltage.setValue(self.values.getEntry("minVoltage"))
        self.resolution = 1000000
        QMetaObject.connectSlotsByName(CavityLengthScan)
        #all of the rest of the code that I have added is below
        #If any changes are made to the ui, copy everything down
        #and only replace components above the top most comment
        #and replace the retranslateUI function.
        self._today = date.today()
        self._traceNum = 0
        self._rm = visa.ResourceManager()
        self._resource = self._rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD212800749::INSTR',timeout=1)
        self._func_gen = FunctionGenerator(self._resource,"SOUR1")
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._apd = None
        self._timer = None
        self._active = False
        self._values = None
        #for timed channel
        self.timedList = []
        self.timedValues = []
        self.currentTime = 0
        
        
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
        self.cavityName.setPlainText(QCoreApplication.translate("CavityLengthScan", u"P15F2_planarCavity", None))
        self.labelFolderName.setText(QCoreApplication.translate("CavityLengthScan", u"Folder Name?", None))
        self.labelComments.setText(QCoreApplication.translate("CavityLengthScan", u"Comments?", None))
        self.labelCavityName.setText(QCoreApplication.translate("CavityLengthScan", u"Cavity Name?", None))
        self.labelWhoAreYou.setText(QCoreApplication.translate("CavityLengthScan", u"Who Are you?", None))
        self.comments.setPlainText(QCoreApplication.translate("CavityLengthScan", u"CLS", None))

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
        self.folderName.setPlainText(QCoreApplication.translate("CavityLengthScan", u"Raman", None))
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
    #function for starting the acquisition 
    def start_acq(self):
        print(self.daqList.currentItem().text())
        #in case we want to use the DAQ as the output
        #self.output = signalOutput("Dev1/ao0", 1000000,100)
        #self.worker =  workerOutput(self.output)
        #self.worker.start()
        self._timer = QTimer()
        time = (1/self.frequency.value())*1000
        self._apd = APD_Reader(self.daqList.currentItem().text(),int(self.resolution/(self.frequency.value())),max_val = self.maxVoltage.value(),min_val = self.minVoltage.value(),continuous = False)
        self._apd.start_acquisition()
        self._timer.start(time)
        self._timer.timeout.connect(self.graph_values)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self._active = True
    #function for stopping the acquisition
    def stop_acq(self):
        #self.worker.terminateLoop()
        #self.worker.quit()
        self._apd.stop_acquisition()
        self._apd.close_daq()
        self._apd = None
        self._timer.stop()
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
        self.apd_graph.clear()
        self._values = self._apd.read_values()
        self._apd.stop_acquisition()
        self._apd.start_acquisition()
        if self.timedOrContinuous.isChecked():
            self.currentTime += 1/self.frequency.value()
            self.timedList.append(self.currentTime)
            self.timedValues.append(sum(self._values)/len(self._values))
            self.apd_graph.plot(self.timedList,self.timedValues)
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
        if self.funcGenSwitch.isChecked():
            if self.scanSwitch.isChecked():
                self._func_gen.write_many(['FUNC:SHAP RAMP','VOLT:UNIT VPP',f"FREQ {self.funcGenFrequency.value()}",f"VOLT {self.amplitude.value()}",f"VOLT:OFFS {self.offset.value()}",f"PHAS {self.phase.value()}",'FUNC:RAMP:SYMM 50'])
            else:
                self._func_gen.write_many(['FUNC:SHAP DC','VOLT:UNIT VPP',f"VOLT:OFFS {self.offset.value()}"])
            self._func_gen.write_many(['OUTP ON'])
        else:
            self._func_gen.write_many(['OUTP OFF'])
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

#Feel free to copy and paste the line below in other GUIs you make, just make sure to change names within it
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    CavityLengthScan = QMainWindow()
    ui = Ui_CavityLengthScan()
    ui.setupUi(CavityLengthScan)
    CavityLengthScan.show()
    sys.exit(app.exec_())
    
