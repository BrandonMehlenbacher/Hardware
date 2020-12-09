# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apdWduzLj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from datetime import date

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Thorlabs_APD import APD_Reader
import numpy as np
from statistics import mean
import pyqtgraph as pg
import pyvisa as visa

class Ui_apdMonitor(object):
    """
    The whole point of this gui is to simply monitor data gathered from and APD
    
    simple description of how to run this program
    
    Exec: python ./apd.py from the command line or powershell to initialize the program

    Run: Click the start button to begin acquisition. If no daq channel is specified it will prompt you to do so before it attempts to
    open the GUI. After it is open, the frequency, board input channel, and the max and min voltage can all be changed while running the program
    To stop data acquisition, simply hit the stop button and it will terminate

    
    """
    def setupUi(self, apdMonitor):
        if not apdMonitor.objectName():
            apdMonitor.setObjectName(u"apdMonitor")
        apdMonitor.resize(908, 701)
        self.centralwidget = QWidget(apdMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.apd_graph = pg.PlotWidget(self.centralwidget)
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(QRect(60, 270, 461, 361))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(740, 380, 131, 51))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(740, 440, 131, 51))
        self.stop.setFont(font)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(550, 540, 131, 31))
        self.frequency.setFont(font)
        self.frequency.setMaximum(10000.000000000000000)
        self.frequency.setSingleStep(0.100000000000000)
        
        self.labelFrequency = QLabel(self.centralwidget)
        self.labelFrequency.setObjectName(u"labelFrequency")
        self.labelFrequency.setGeometry(QRect(550, 510, 131, 31))
        self.labelFrequency.setFont(font)
        self.labelDaqList = QLabel(self.centralwidget)
        self.labelDaqList.setObjectName(u"labelDaqList")
        self.labelDaqList.setGeometry(QRect(550, 440, 131, 31))
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
        QListWidgetItem(self.daqList)
        self.daqList.setObjectName(u"daqList")
        self.daqList.setGeometry(QRect(550, 470, 111, 31))
        self.daqList.setFont(font)
        self.daqList.setSortingEnabled(False)
        self.minVoltage = QDoubleSpinBox(self.centralwidget)
        self.minVoltage.setObjectName(u"minVoltage")
        self.minVoltage.setGeometry(QRect(550, 410, 131, 21))
        self.minVoltage.setFont(font)
        self.labelMinVoltage = QLabel(self.centralwidget)
        self.labelMinVoltage.setObjectName(u"labelMinVoltage")
        self.labelMinVoltage.setGeometry(QRect(550, 380, 161, 31))
        self.labelMinVoltage.setFont(font)
        self.labelMaxVoltage = QLabel(self.centralwidget)
        self.labelMaxVoltage.setObjectName(u"labelMaxVoltage")
        self.labelMaxVoltage.setGeometry(QRect(550, 320, 181, 31))
        self.labelMaxVoltage.setFont(font)
        self.maxVoltage = QDoubleSpinBox(self.centralwidget)
        self.maxVoltage.setObjectName(u"maxVoltage")
        self.maxVoltage.setGeometry(QRect(550, 360, 131, 21))
        self.maxVoltage.setFont(font)
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
        self.whoAreYou.setGeometry(QRect(30, 130, 161, 41))
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
        self.save.setGeometry(QRect(740, 520, 131, 51))
        self.save.setFont(font)
        apdMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(apdMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 908, 26))
        apdMonitor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(apdMonitor)
        self.statusbar.setObjectName(u"statusbar")
        apdMonitor.setStatusBar(self.statusbar)
        self.checkSweepFrequency = QCheckBox(self.centralwidget)
        self.checkSweepFrequency.setObjectName(u"checkSweepFrequency")
        self.checkSweepFrequency.setGeometry(QRect(740, 270, 121, 41))
        self.checkSweepFrequency.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(740, 310, 131, 31))
        self.label.setFont(font)
        self.sweepFrequency = QDoubleSpinBox(self.centralwidget)
        self.sweepFrequency.setObjectName(u"sweepFrequency")
        self.sweepFrequency.setGeometry(QRect(740,340,131,31))
        self.sweepFrequency.setFont(font)
        
        self.sweepFrequency.setValue(40)
        self.frequency.setValue(10.000000000000000)
        self.maxVoltage.setValue(10)
        self.minVoltage.setValue(0)
        self.retranslateUi(apdMonitor)
        
        QMetaObject.connectSlotsByName(apdMonitor)
        #all of the rest of the code that I have added is below
        #If any changes are made to the ui, copy everything down
        #and only replace components above the top most comment
        #and replace the retranslateUI function.
        self._today = date.today()
        self._traceNum = 0
        self._rm = visa.ResourceManager()
        self._func_gen = self._rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD212800749::INSTR',timeout=1)
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._apd = None
        self._timer = None
        self._active = False
        self._values = None
        QMetaObject.connectSlotsByName(apdMonitor)
        self.frequency.valueChanged.connect(self.change_value)
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        self.daqList.currentItemChanged.connect(self.change_value)
        self.maxVoltage.valueChanged.connect(self.change_value)
        self.minVoltage.valueChanged.connect(self.change_value)
        self.checkSweepFrequency.stateChanged.connect(self.func_generation)

        self.save.clicked.connect(self.save_values)
    def retranslateUi(self, apdMonitor):
        apdMonitor.setWindowTitle(QCoreApplication.translate("apdMonitor", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("apdMonitor", u"Start", None))
        self.stop.setText(QCoreApplication.translate("apdMonitor", u"Stop", None))
        self.labelFrequency.setText(QCoreApplication.translate("apdMonitor", u"Frequency", None))
        self.labelDaqList.setText(QCoreApplication.translate("apdMonitor", u"DAQ Channel", None))

        __sortingEnabled = self.daqList.isSortingEnabled()
        self.daqList.setSortingEnabled(False)
        ___qlistwidgetitem = self.daqList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai0", None));
        ___qlistwidgetitem1 = self.daqList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai1", None));
        ___qlistwidgetitem2 = self.daqList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai2", None));
        ___qlistwidgetitem3 = self.daqList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai3", None));
        ___qlistwidgetitem4 = self.daqList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai4", None));
        ___qlistwidgetitem5 = self.daqList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai5", None));
        ___qlistwidgetitem6 = self.daqList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai6", None));
        ___qlistwidgetitem7 = self.daqList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai7", None));
        ___qlistwidgetitem8 = self.daqList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("apdMonitor", u"Dev1/ai8", None));
        self.daqList.setSortingEnabled(__sortingEnabled)

        self.labelMinVoltage.setText(QCoreApplication.translate("apdMonitor", u"Minimum Voltage", None))
        self.labelMaxVoltage.setText(QCoreApplication.translate("apdMonitor", u"Maximum Voltage", None))
        self.cavityName.setPlainText(QCoreApplication.translate("apdMonitor", u"F15P2_Planar", None))
        self.labelFolderName.setText(QCoreApplication.translate("apdMonitor", u"Folder Name?", None))
        self.labelComments.setText(QCoreApplication.translate("apdMonitor", u"Comments?", None))
        self.labelCavityName.setText(QCoreApplication.translate("apdMonitor", u"Cavity Name?", None))
        self.labelWhoAreYou.setText(QCoreApplication.translate("apdMonitor", u"Who Are you?", None))
        self.comments.setPlainText("")

        __sortingEnabled1 = self.whoAreYou.isSortingEnabled()
        self.whoAreYou.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.whoAreYou.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("apdMonitor", u"Brandon Mehlenbacher", None));
        ___qlistwidgetitem10 = self.whoAreYou.item(1)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("apdMonitor", u"Lisa-Maria", None));
        ___qlistwidgetitem11 = self.whoAreYou.item(2)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("apdMonitor", u"Beau", None));
        ___qlistwidgetitem12 = self.whoAreYou.item(3)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("apdMonitor", u"Ceci", None));
        ___qlistwidgetitem13 = self.whoAreYou.item(4)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("apdMonitor", u"Levi", None));
        self.whoAreYou.setSortingEnabled(__sortingEnabled1)

        self.labelFileLocationPath.setText(QCoreApplication.translate("apdMonitor", u"File Location Path", None))
        self.localOrDatabackup.setText(QCoreApplication.translate("apdMonitor", u"Local (T) / Databackup (F)", None))
        self.folderName.setPlainText(QCoreApplication.translate("apdMonitor", u"Raman", None))
        self.save.setText(QCoreApplication.translate("apdMonitor", u"Save", None))
        self.checkSweepFrequency.setText(QCoreApplication.translate("apdMonitor", u"Sweep Laser", None))

        self.label.setText(QCoreApplication.translate("apdMonitor", u"Sweep Frequency", None))

    #function for starting the acquisition 
    def start_acq(self):
        print(self.daqList.currentItem().text())
        self._apd = APD_Reader(self.daqList.currentItem().text(),int(1000000/(self.frequency.value()/2)),max_val = self.maxVoltage.value(),min_val = self.minVoltage.value())
        self._apd.start_acquisition()
        self._timer = QTimer()
        time = (1/self.frequency.value())*1000
        #self._timed_values= np.zeros(int(3600/time))
        #self._max_count = self._timed_values.size
        #self.counter = 0
        self._timer.start(time)
        self._timer.timeout.connect(self.graph_values)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self._active = True

    #function for stopping the acquisition
    def stop_acq(self):
        self._apd.stop_acquisition()
        self._apd.close_daq()
        self._apd = None
        self._timer.stop()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._active = False
        
    #if any of the values have changed, everything gets reset if the DAQ is actually active, if not ignores it
    def change_value(self):
        if self._active:
            self._apd.stop_acquisition()
            self._apd.close_daq()
            self._apd = None
            self._apd = APD_Reader(self.daqList.currentItem().text(),int(1000000/(self.frequency.value()/2)),max_val = self.maxVoltage.value(),min_val = self.minVoltage.value(),)
            self._apd.start_acquisition()
            time = (1/self.frequency.value())*1000
            self._timer.start(time)
            self._timer.timeout.connect(self.graph_values)
    #plots all of the values from the APD in the pyqtplot
    def graph_values(self):
        self.apd_graph.clear()
        self._values = self._apd.read_values()
        #self._timed_values[self.counter] = mean(self._values)
        #self.counter += 1;
        self.apd_graph.plot(self._values)
    def save_values(self):
        self._traceNum+=1;
        stopped = False
        if self._active:
            self.stop_acq()
            stopped = True
        if self.localOrDatabackup.isChecked():
            current_directory = os.getcwd()
            directory = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()
            self._filename = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()+f"resonance_{self._traceNum}.csv"
            self.fileLocationPath.setPlainText(self._filename)
        else:
            current_directory = "//marlin.chem.wisc.edu/Groups/Goldsmith Group/X/dataBackup/ELN_Data"
            directory = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()
            self._filename = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()+f"resonance_{self._traceNum}.csv"
            self.fileLocationPath.setPlainText(self._filename)
        saveValues = np.array(self._values)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        np.savetxt(self._filename,saveValues)
        np.savetxt(self._filename,self._timed_values)
        if stopped:
            self.start_acq()
    def func_generation(self):
        if self.checkSweepFrequency.isChecked():
            self._func_gen.write(f':SOUR1:;FUNC:SHAP RAMP;:VOLT:UNIT VPP;:FREQ {self.sweepFrequency.value()};:VOLT 1;:SYMM 50')
            self._func_gen.write(':SOUR1;:OUTP ON;')
        else:
            self._func_gen.write(':SOUR1;:OUTP OFF;')

#Feel free to copy and paste the line below in other GUIs you make, just make sure to change names within it
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apdMonitor = QMainWindow()
    ui = Ui_apdMonitor()
    ui.setupUi(apdMonitor)
    apdMonitor.show()
    sys.exit(app.exec_())
    
