import sys
import os
from datetime import date
#path = os.getcwd()
#parent = getParent(path,levels=1)
#print(parent)
sys.path.append(r"C:\Users\Goldsmith\Desktop\Hardware") # this adds a path to the hardware directory so I have access to all of the different packages I make

import pandas as pd
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from APD_Control.Thorlabs_APD import APD_Reader
from Q_Calc import QFactor
import numpy as np
import pyqtgraph as pg
from FFPC_Programs.initialValues import initializeValues
import pyvisa as visa


class Ui_QMonitor(object):
    
    def __init__(self):
        names = ['frequency','minVoltage','maxVoltage','sweepFrequency','resolution']
        self.values = initializeValues(names)
        
    def setupUi(self, QMonitor):
        if not QMonitor.objectName():
            QMonitor.setObjectName(u"QMonitor")
        QMonitor.resize(942, 723)
        self.centralwidget = QWidget(QMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.apd_graph = pg.PlotWidget(self.centralwidget)
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(
            QRect(50, 270, 461, 371))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(
            QRect(760, 350, 131, 51))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(
            QRect(760, 430, 131, 51))
        self.stop.setFont(font)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(
            QRect(760, 300, 131, 31))
        self.frequency.setFont(font)
        self.frequency.setMaximum(10000.000000000000000)
        self.frequency.setSingleStep(0.100000000000000)
        self.frequency.setValue(10.000000000000000)
        self.labelFrequency = QLabel(self.centralwidget)
        self.labelFrequency.setObjectName(u"label_frequency")
        self.labelFrequency.setGeometry(
            QRect(760, 270, 131, 31))
        self.labelFrequency.setFont(font)
        self.labelDaqList = QLabel(self.centralwidget)
        self.labelDaqList.setObjectName(u"label_daqList")
        self.labelDaqList.setGeometry(
            QRect(570, 410, 131, 31))
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
        self.daqList.setGeometry(
            QRect(570, 450, 111, 31))
        self.daqList.setFont(font)
        self.daqList.setSortingEnabled(False)
        self.minVoltage = QDoubleSpinBox(self.centralwidget)
        self.minVoltage.setObjectName(u"min_voltage")
        self.minVoltage.setGeometry(
            QRect(570, 370, 131, 31))
        self.minVoltage.setFont(font)
        self.minVoltage.setMinimum(-10.000000000000000)
        self.labelMinVoltage = QLabel(self.centralwidget)
        self.labelMinVoltage.setObjectName(u"labelMinVoltage")
        self.labelMinVoltage.setGeometry(
            QRect(570, 340, 171, 31))
        self.labelMinVoltage.setFont(font)
        self.labelMaxVoltage = QLabel(self.centralwidget)
        self.labelMaxVoltage.setObjectName(u"labelMaxVoltage")
        self.labelMaxVoltage.setGeometry(
            QRect(570, 270, 171, 31))
        self.labelMaxVoltage.setFont(font)
        self.maxVoltage = QDoubleSpinBox(self.centralwidget)
        self.maxVoltage.setObjectName(u"maxVoltage")
        self.maxVoltage.setGeometry(
            QRect(570, 300, 131, 31))
        self.maxVoltage.setFont(font)
        self.valueQFactor = QLCDNumber(self.centralwidget)
        self.valueQFactor.setObjectName(u"valueQFactor")
        self.valueQFactor.setGeometry(
            QRect(760, 590, 131, 51))
        self.pushQFactor = QPushButton(self.centralwidget)
        self.pushQFactor.setObjectName(u"pushQFactor")
        self.pushQFactor.setGeometry(
            QRect(570, 590, 121, 51))
        self.pushQFactor.setFont(font)
        self.labelQFactor = QLabel(self.centralwidget)
        self.labelQFactor.setObjectName(u"labelQFactor")
        self.labelQFactor.setGeometry(
            QRect(760, 560, 131, 31))
        self.labelQFactor.setFont(font)
        self.whoAreYou = QListWidget(self.centralwidget)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        self.whoAreYou.setObjectName(u"whoAreYou")
        self.whoAreYou.setGeometry(
            QRect(50, 140, 161, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.whoAreYou.setFont(font1)
        self.labelWhoAreYou = QLabel(self.centralwidget)
        self.labelWhoAreYou.setObjectName(u"labelWhoAreYou")
        self.labelWhoAreYou.setGeometry(
            QRect(50, 110, 121, 21))
        self.labelWhoAreYou.setFont(font1)
        self.localOrDatabackup = QCheckBox(self.centralwidget)
        self.localOrDatabackup.setObjectName(u"localOrDatabackup")
        self.localOrDatabackup.setGeometry(
            QRect(50, 210, 241, 31))
        self.localOrDatabackup.setFont(font1)
        self.cavityName = QPlainTextEdit(self.centralwidget)
        self.cavityName.setObjectName(u"cavityName")
        self.cavityName.setGeometry(
            QRect(240, 140, 291, 41))
        self.cavityName.setFont(font1)
        self.labelCavityName = QLabel(self.centralwidget)
        self.labelCavityName.setObjectName(u"labelCavityName")
        self.labelCavityName.setGeometry(
            QRect(240, 110, 131, 16))
        self.labelCavityName.setFont(font1)
        self.folderName = QPlainTextEdit(self.centralwidget)
        self.folderName.setObjectName(u"folderName")
        self.folderName.setGeometry(
            QRect(560, 140, 331, 41))
        self.folderName.setFont(font1)
        self.labelFolderName = QLabel(self.centralwidget)
        self.labelFolderName.setObjectName(u"labelFolderName")
        self.labelFolderName.setGeometry(
            QRect(560, 110, 131, 16))
        self.labelFolderName.setFont(font1)
        self.comments = QPlainTextEdit(self.centralwidget)
        self.comments.setObjectName(u"comments")
        self.comments.setGeometry(
            QRect(560, 220, 331, 41))
        self.comments.setFont(font1)
        self.labelComments = QLabel(self.centralwidget)
        self.labelComments.setObjectName(u"labelComments")
        self.labelComments.setGeometry(
            QRect(560, 190, 131, 16))
        self.labelComments.setFont(font1)
        self.fileLocationPath = QPlainTextEdit(self.centralwidget)
        self.fileLocationPath.setObjectName(u"fileLocationPath")
        self.fileLocationPath.setGeometry(
            QRect(50, 50, 841, 41))
        self.fileLocationPath.setFont(font1)
        self.labelFileLocationPath = QLabel(self.centralwidget)
        self.labelFileLocationPath.setObjectName(u"labelFileLocationPath")
        self.labelFileLocationPath.setGeometry(
            QRect(50, 20, 231, 16))
        self.labelFileLocationPath.setFont(font1)
        self.sweepFrequency = QDoubleSpinBox(self.centralwidget)
        self.sweepFrequency.setObjectName(u"sweepFrequency")
        self.sweepFrequency.setGeometry(
            QRect(570, 530, 131, 31))
        self.sweepFrequency.setFont(font)
        self.sweepFrequency.setMaximum(1000.000000000000000)
        self.labelSweepFrequency = QLabel(self.centralwidget)
        self.labelSweepFrequency.setObjectName(u"labelSweepFrequency")
        self.labelSweepFrequency.setGeometry(
            QRect(570, 490, 171, 31))
        self.labelSweepFrequency.setFont(font)
        self.labelResolution = QLabel(self.centralwidget)
        self.labelResolution.setObjectName(u"labelResolution")
        self.labelResolution.setGeometry(
            QRect(760, 490, 171, 31))
        self.labelResolution.setFont(font)
        self.resolution = QSpinBox(self.centralwidget)
        self.resolution.setObjectName(u"resolution")
        self.resolution.setGeometry(
            QRect(760, 530, 131, 31))
        self.resolution.setFont(font)
        self.resolution.setMaximum(1000000)
        QMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(
            QRect(0, 0, 942, 26))
        QMonitor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QMonitor)
        self.statusbar.setObjectName(u"statusbar")
        QMonitor.setStatusBar(self.statusbar)

        self.retranslateUi(QMonitor)
        
        # keep all of the setting values
        self.frequency.setValue(self.values.getEntry("frequency"))
        self.minVoltage.setValue(self.values.getEntry("minVoltage"))
        self.maxVoltage.setValue(self.values.getEntry("maxVoltage"))
        self.sweepFrequency.setValue(self.values.getEntry("sweepFrequency"))
        self.resolution.setValue(self.values.getEntry("resolution"))
        
        QMetaObject.connectSlotsByName(QMonitor)
        self._rm = visa.ResourceManager()
        self._func_gen = self._rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD212800749::INSTR',timeout=1)
        
        # all of the rest of the code that I have added is below
        # If any changes are made to the ui, copy everything down
        # and only replace components above the top most comment
        # and replace the retranslateUI function.
        self._today = date.today()
        
        self._traceNum = 0
        self._filename = ""
        self._correction = int(self.resolution.value()/self.sweepFrequency.value())
        self.fileLocationPath.setPlainText(self._filename)
        self.start.setEnabled(True)
        self.stop.setEnabled(True)
        self._apd = None
        self._timer = None
        self._active = False
        self._QCalc = None
        
        QMetaObject.connectSlotsByName(QMonitor)

        self.frequency.valueChanged.connect(self.change_value)
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        self.daqList.currentItemChanged.connect(self.change_value)
        self.maxVoltage.valueChanged.connect(self.change_value)
        self.minVoltage.valueChanged.connect(self.change_value)
        self.pushQFactor.clicked.connect(self.qFactor)
        self.whoAreYou.currentItemChanged.connect(self.change_filename)
        self.cavityName.textChanged.connect(self.change_filename)
        self.folderName.textChanged.connect(self.change_filename)
        self.comments.textChanged.connect(self.change_filename)

    def retranslateUi(self, QMonitor):
        QMonitor.setWindowTitle(QCoreApplication.translate("QMonitor", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("QMonitor", u"Start", None))
        self.stop.setText(QCoreApplication.translate("QMonitor", u"Stop", None))
        self.labelFrequency.setText(QCoreApplication.translate("QMonitor", u"Frequency", None))
        self.labelDaqList.setText(QCoreApplication.translate("QMonitor", u"DAQ Channel", None))

        __sortingEnabled = self.daqList.isSortingEnabled()
        self.daqList.setSortingEnabled(False)
        ___qlistwidgetitem = self.daqList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai0", None))
        ___qlistwidgetitem1 = self.daqList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai1", None))
        ___qlistwidgetitem2 = self.daqList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai2", None))
        ___qlistwidgetitem3 = self.daqList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai3", None))
        ___qlistwidgetitem4 = self.daqList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai4", None))
        ___qlistwidgetitem5 = self.daqList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai5", None))
        ___qlistwidgetitem6 = self.daqList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai6", None))
        ___qlistwidgetitem7 = self.daqList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai7", None))
        ___qlistwidgetitem8 = self.daqList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai8", None))
        self.daqList.setSortingEnabled(__sortingEnabled)

        self.labelMinVoltage.setText(QCoreApplication.translate("QMonitor", u"Minimum Voltage", None))
        self.labelMaxVoltage.setText(QCoreApplication.translate("QMonitor", u"Maximum Voltage", None))
        self.pushQFactor.setText(QCoreApplication.translate("QMonitor", u"Q-Factor", None))
        self.labelQFactor.setText(QCoreApplication.translate("QMonitor", u"Q-Factor", None))

        __sortingEnabled1 = self.whoAreYou.isSortingEnabled()
        self.whoAreYou.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.whoAreYou.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("QMonitor", u"Brandon Mehlenbacher", None))
        ___qlistwidgetitem10 = self.whoAreYou.item(1)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("QMonitor", u"Lisa-Maria", None))
        ___qlistwidgetitem11 = self.whoAreYou.item(2)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("QMonitor", u"Beau", None))
        ___qlistwidgetitem12 = self.whoAreYou.item(3)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("QMonitor", u"Ceci", None))
        ___qlistwidgetitem13 = self.whoAreYou.item(4)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("QMonitor", u"Levi", None))
        self.whoAreYou.setSortingEnabled(__sortingEnabled1)

        self.labelWhoAreYou.setText(
            QCoreApplication.translate("QMonitor", u"Who Are you?", None))
        self.localOrDatabackup.setText(
            QCoreApplication.translate("QMonitor", u"Local (T) / Databackup (F)", None))
        self.cavityName.setPlainText(
            QCoreApplication.translate("QMonitor", u"P15F2_planarCavity", None))
        self.labelCavityName.setText(
            QCoreApplication.translate("QMonitor", u"Cavity Name?", None))
        self.folderName.setPlainText(
            QCoreApplication.translate("QMonitor", u"Raman", None))
        self.labelFolderName.setText(
            QCoreApplication.translate("QMonitor", u"Folder Name?", None))
        self.comments.setPlainText("")
        self.labelComments.setText(
            QCoreApplication.translate("QMonitor", u"Comments?", None))
        self.labelFileLocationPath.setText(
            QCoreApplication.translate("QMonitor", u"File Location Path", None))
        self.labelSweepFrequency.setText(
            QCoreApplication.translate("QMonitor", u"Sweep Frequency", None))
        self.labelResolution.setText(
            QCoreApplication.translate("QMonitor", u"Resolution", None))

    # function for starting the acquisition
    def start_acq(self):
        #try:
        if self._active:
            self._apd.start_acquisition()
        else:
            print(self.daqList.currentItem().text())
            self._apd = APD_Reader(self.daqList.currentItem().text(),
                                   int(self._correction),
                                   max_val=self.maxVoltage.value(),
                                   min_val=self.minVoltage.value(),
                                   continuous=False)
            self._apd.start_acquisition()
            self._timer = QTimer()
            self._active = True
            self._func_gen.write(f':SOUR1:;FUNC:SHAP RAMP;:VOLT:UNIT VPP;:FREQ {self.sweepFrequency.value()};:VOLT 1;FUNC:RAMP:SYMM 50;')
            self._func_gen.write(':SOUR1;:OUTP ON;')
        #except AttributeError:
        #    print("Make sure you selected a daq channel")

    # function for stopping the acquisition
    def stop_acq(self):
        if self._active:
            self._apd.close_daq()
            self._apd = None
            self._active = False
            self._func_gen.write(':SOUR1;:OUTP OFF;')

    # if any of the values have changed, everything gets reset if the DAQ is actually active, if not ignores it
    def change_value(self):
        listValues = [self.frequency.value(),
                        self.minVoltage.value(),
                        self.maxVoltage.value(),
                        self.sweepFrequency.value(),
                        self.resolution.value(),
                      ]
        self.values.saveValues(listValues)
        if self._active:
            # this is the list of values we will track, need to be same order as names
            self._apd.stop_acquisition()
            self._apd.close_daq()
            self._apd = None
            self._apd = APD_Reader(self.daqList.currentItem().text(),
                                   int(self._correction),
                                   max_val=self.maxVoltage.value(),
                                   min_val=self.minVoltage.value(),
                                   )
            self._apd.start_acquisition()

    # plots all of the values from the APD in the pyqtplot
    def qFactor(self):
        if self._active:
            self._correction = int(self.resolution.value()/self.sweepFrequency.value())
            self._x_values = (120.5/self._correction)*np.array(range(self._correction))
            self.apd_graph.clear()
            values = self._apd.read_values()
            x_values = self._x_values[0:int(len(self._x_values)/2)]
            y_values = values[0:int(len(self._x_values)/2)]
            dataframe = pd.DataFrame({'x_values': x_values, 'y_values': y_values})
            self.apd_graph.plot(x_values, y_values)
            self._QCalc = QFactor(x_values, y_values)
            self._QCalc.fitLorentz()
            sigma = self._QCalc.getSigma()
            self._apd.stop_acquisition()
            self.valueQFactor.display(780000/sigma)  # roughly the wavelength in picometers
            newYValues = self._QCalc.getNewYVal()
            self.apd_graph.plot(x_values, newYValues)
            dataframe.to_csv(self._filename)
            self.change_filename()
            self._traceNum+=1;
            
            

    def change_filename(self):
        if self.localOrDatabackup.isChecked():
            current_directory = os.getcwd()
            directory = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()
            self._filename = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()+f"QFactor_{self._traceNum}.csv"
            self.fileLocationPath.setPlainText(self._filename)
        else:
            current_directory = "//marlin.chem.wisc.edu/Groups/Goldsmith Group/X/dataBackup/ELN_Data"
            directory = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()
            self._filename = current_directory+"/"+self.whoAreYou.currentItem().text()+"/"+self.folderName.toPlainText()+"/"+str(self._today)+"/"+self.cavityName.toPlainText()+"/"+self.comments.toPlainText()+f"QFactor_{self._traceNum}.csv"
            self.fileLocationPath.setPlainText(self._filename)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        
# Feel free to copy and paste the line below in other GUIs you make
# just make sure to change names within it
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    QMonitor = QMainWindow()
    ui = Ui_QMonitor()
    ui.setupUi(QMonitor)
    QMonitor.show()
    sys.exit(app.exec_())
