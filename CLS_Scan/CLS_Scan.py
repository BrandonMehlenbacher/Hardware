# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CLS_ScanMpcKZV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
sys.path.append(r"C:\Users\Goldsmith\Desktop\Hardware")
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import nidaqmx as daq
from nidaqmx.stream_writers import AnalogSingleChannelWriter
from scipy.signal import sawtooth
from APD_Control.Thorlabs_APD import APD_Reader
from signalOutput import signalOutput, workerOutput
import pyqtgraph as pg
#Eventually I will read these values in and save them before exiting so this becomes unnecessary but thats a pipe dream as of now
initial_amplitude = 0.2
initial_frequency = 10
initial_offset = 0.200 #? I am not sure what this is supposed to be
initial_phase = 270
outputChannel = "Dev1/ao0"
#
class Ui_CLS_Scan(object):
    def setupUi(self, CLS_Scan):
        if not CLS_Scan.objectName():
            CLS_Scan.setObjectName(u"CLS_Scan")
        CLS_Scan.resize(561, 666)
        self.centralwidget = QWidget(CLS_Scan)
        self.centralwidget.setObjectName(u"centralwidget")
        self.clsPlot = pg.PlotWidget(self.centralwidget)#QGraphicsView(self.centralwidget)
        self.clsPlot.setObjectName(u"clsPlot")
        self.clsPlot.setGeometry(QRect(30, 330, 351, 251))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        self.clsPlot.setFont(font)
        self.labelCLSPlot = QLabel(self.centralwidget)
        self.labelCLSPlot.setObjectName(u"labelCLSPlot")
        self.labelCLSPlot.setGeometry(QRect(30, 310, 191, 16))
        self.labelCLSPlot.setFont(font)
        self.offset = QDoubleSpinBox(self.centralwidget)
        self.offset.setObjectName(u"offset")
        self.offset.setGeometry(QRect(310, 290, 71, 22))
        self.offset.setFont(font)
        self.offset.setSingleStep(0.010000000000000)
        self.offset.setValue(0.200000000000000)
        self.phase = QDoubleSpinBox(self.centralwidget)
        self.phase.setObjectName(u"phase")
        self.phase.setGeometry(QRect(420, 290, 71, 22))
        self.phase.setFont(font)
        self.phase.setMaximum(360.000000000000000)
        self.phase.setValue(270.000000000000000)
        self.amplitude = QDoubleSpinBox(self.centralwidget)
        self.amplitude.setObjectName(u"amplitude")
        self.amplitude.setGeometry(QRect(310, 240, 71, 22))
        self.amplitude.setFont(font)
        self.amplitude.setSingleStep(0.010000000000000)
        self.amplitude.setValue(0.200000000000000)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(420, 240, 71, 22))
        self.frequency.setFont(font)
        self.frequency.setValue(10.000000000000000)
        self.labelAmplitude = QLabel(self.centralwidget)
        self.labelAmplitude.setObjectName(u"labelAmplitude")
        self.labelAmplitude.setGeometry(QRect(310, 220, 71, 16))
        self.labelAmplitude.setFont(font)
        self.labelFrequency = QLabel(self.centralwidget)
        self.labelFrequency.setObjectName(u"labelFrequency")
        self.labelFrequency.setGeometry(QRect(420, 220, 71, 16))
        self.labelFrequency.setFont(font)
        self.labelOffset = QLabel(self.centralwidget)
        self.labelOffset.setObjectName(u"labelOffset")
        self.labelOffset.setGeometry(QRect(310, 270, 71, 16))
        self.labelOffset.setFont(font)
        self.labelPhase = QLabel(self.centralwidget)
        self.labelPhase.setObjectName(u"labelPhase")
        self.labelPhase.setGeometry(QRect(420, 270, 71, 16))
        self.labelPhase.setFont(font)
        self.waitTime = QDoubleSpinBox(self.centralwidget)
        self.waitTime.setObjectName(u"waitTime")
        self.waitTime.setGeometry(QRect(420, 340, 71, 22))
        self.waitTime.setFont(font)
        self.labelWaitTime = QLabel(self.centralwidget)
        self.labelWaitTime.setObjectName(u"labelWaitTime")
        self.labelWaitTime.setGeometry(QRect(420, 320, 71, 16))
        self.labelWaitTime.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(410, 450, 111, 51))
        self.stop.setFont(font)
        self.capture = QPushButton(self.centralwidget)
        self.capture.setObjectName(u"capture")
        self.capture.setGeometry(QRect(410, 510, 111, 51))
        self.capture.setFont(font)
        self.whoAreYou = QListWidget(self.centralwidget)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        QListWidgetItem(self.whoAreYou)
        self.whoAreYou.setObjectName(u"whoAreYou")
        self.whoAreYou.setGeometry(QRect(30, 160, 231, 31))
        self.whoAreYou.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 140, 101, 16))
        self.label.setFont(font)
        self.labelCavity = QLabel(self.centralwidget)
        self.labelCavity.setObjectName(u"labelCavity")
        self.labelCavity.setGeometry(QRect(300, 140, 55, 16))
        self.labelCavity.setFont(font)
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
        self.daqList.setGeometry(QRect(30, 220, 111, 31))
        self.daqList.setFont(font)
        self.labelDaqChannel = QLabel(self.centralwidget)
        self.labelDaqChannel.setObjectName(u"labelDaqChannel")
        self.labelDaqChannel.setGeometry(QRect(30, 200, 111, 16))
        self.labelDaqChannel.setFont(font)
        self.singleChannelM = QDoubleSpinBox(self.centralwidget)
        self.singleChannelM.setObjectName(u"singleChannelM")
        self.singleChannelM.setGeometry(QRect(30, 280, 62, 22))
        self.singleChannelM.setFont(font)
        self.singleChannelM.setValue(10.000000000000000)
        self.singleChannelM2 = QDoubleSpinBox(self.centralwidget)
        self.singleChannelM2.setObjectName(u"singleChannelM2")
        self.singleChannelM2.setGeometry(QRect(170, 280, 62, 22))
        self.singleChannelM2.setFont(font)
        self.singleChannelM2.setValue(10.000000000000000)
        self.labelSingleChannelM = QLabel(self.centralwidget)
        self.labelSingleChannelM.setObjectName(u"labelSingleChannelM")
        self.labelSingleChannelM.setGeometry(QRect(30, 260, 111, 16))
        self.labelSingleChannelM.setFont(font)
        self.labelSingleChannelM2 = QLabel(self.centralwidget)
        self.labelSingleChannelM2.setObjectName(u"labelSingleChannelM2")
        self.labelSingleChannelM2.setGeometry(QRect(170, 260, 111, 16))
        self.labelSingleChannelM2.setFont(font)
        self.cavityName = QTextEdit(self.centralwidget)
        self.cavityName.setObjectName(u"cavityName")
        self.cavityName.setGeometry(QRect(300, 160, 191, 31))
        self.cavityName.setFont(font)
        self.folderName = QPlainTextEdit(self.centralwidget)
        self.folderName.setObjectName(u"folderName")
        self.folderName.setGeometry(QRect(30, 100, 231, 31))
        self.folderName.setFont(font)
        self.labelSavingFolder = QLabel(self.centralwidget)
        self.labelSavingFolder.setObjectName(u"labelSavingFolder")
        self.labelSavingFolder.setGeometry(QRect(30, 80, 181, 16))
        self.labelSavingFolder.setFont(font)
        self.filenameComments = QPlainTextEdit(self.centralwidget)
        self.filenameComments.setObjectName(u"filenameComments")
        self.filenameComments.setGeometry(QRect(300, 100, 191, 31))
        self.filenameComments.setFont(font)
        self.labelFilenameComments = QLabel(self.centralwidget)
        self.labelFilenameComments.setObjectName(u"labelFilenameComments")
        self.labelFilenameComments.setGeometry(QRect(300, 80, 131, 16))
        self.labelFilenameComments.setFont(font)
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(410, 390, 111, 51))
        self.start.setFont(font)
        self.folderName_2 = QPlainTextEdit(self.centralwidget)
        self.folderName_2.setObjectName(u"folderName_2")
        self.folderName_2.setGeometry(QRect(30, 40, 461, 31))
        self.folderName_2.setFont(font)
        self.fileLocationPath = QLabel(self.centralwidget)
        self.fileLocationPath.setObjectName(u"fileLocationPath")
        self.fileLocationPath.setGeometry(QRect(30, 20, 181, 16))
        self.fileLocationPath.setFont(font)
        CLS_Scan.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CLS_Scan)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 21))
        CLS_Scan.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CLS_Scan)
        self.statusbar.setObjectName(u"statusbar")
        CLS_Scan.setStatusBar(self.statusbar)

        self.retranslateUi(CLS_Scan)
        self.daqList.setCurrentRow(0)
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        

        self._daqOutput = None
        self._APD = None
        self._daqActive = False
        self._started = False
        self._samples = None
        self._timer = None
        QMetaObject.connectSlotsByName(CLS_Scan)
        
        #this will be where all of my code will go
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        #self.frequency.valueChanged.connect(self.value_change)
        #self.amplitude.valueChanged.connect(self.value_change)
        #self.offset.valueChanged.connect(self.value_change)
    # setupUi

    def retranslateUi(self, CLS_Scan):
        CLS_Scan.setWindowTitle(QCoreApplication.translate("CLS_Scan", u"MainWindow", None))
        self.labelCLSPlot.setText(QCoreApplication.translate("CLS_Scan", u"CLS Scan", None))
        self.labelAmplitude.setText(QCoreApplication.translate("CLS_Scan", u"Amplitude", None))
        self.labelFrequency.setText(QCoreApplication.translate("CLS_Scan", u"Frequency", None))
        self.labelOffset.setText(QCoreApplication.translate("CLS_Scan", u"Offset", None))
        self.labelPhase.setText(QCoreApplication.translate("CLS_Scan", u"Phase", None))
        self.labelWaitTime.setText(QCoreApplication.translate("CLS_Scan", u"Wait Time", None))
        self.stop.setText(QCoreApplication.translate("CLS_Scan", u"Stop", None))
        self.capture.setText(QCoreApplication.translate("CLS_Scan", u"Capture", None))

        __sortingEnabled = self.whoAreYou.isSortingEnabled()
        self.whoAreYou.setSortingEnabled(False)
        ___qlistwidgetitem = self.whoAreYou.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("CLS_Scan", u"Brandon Mehlenbacher", None));
        ___qlistwidgetitem1 = self.whoAreYou.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("CLS_Scan", u"Ceci", None));
        ___qlistwidgetitem2 = self.whoAreYou.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("CLS_Scan", u"Beau", None));
        ___qlistwidgetitem3 = self.whoAreYou.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("CLS_Scan", u"Lisa-Maria", None));
        self.whoAreYou.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("CLS_Scan", u"Who Are You", None))
        self.labelCavity.setText(QCoreApplication.translate("CLS_Scan", u"Cavity", None))

        __sortingEnabled1 = self.daqList.isSortingEnabled()
        self.daqList.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.daqList.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai0", None));
        ___qlistwidgetitem5 = self.daqList.item(1)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai1", None));
        ___qlistwidgetitem6 = self.daqList.item(2)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai2", None));
        ___qlistwidgetitem7 = self.daqList.item(3)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai3", None));
        ___qlistwidgetitem8 = self.daqList.item(4)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai4", None));
        ___qlistwidgetitem9 = self.daqList.item(5)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai5", None));
        ___qlistwidgetitem10 = self.daqList.item(6)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai6", None));
        ___qlistwidgetitem11 = self.daqList.item(7)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("CLS_Scan", u"Dev1/ai7", None));
        self.daqList.setSortingEnabled(__sortingEnabled1)

        self.labelDaqChannel.setText(QCoreApplication.translate("CLS_Scan", u"DAQ Channel", None))
        self.labelSingleChannelM.setText(QCoreApplication.translate("CLS_Scan", u"Single Channel M", None))
        self.labelSingleChannelM2.setText(QCoreApplication.translate("CLS_Scan", u"Single Channel M", None))
        self.labelSavingFolder.setText(QCoreApplication.translate("CLS_Scan", u"Saving Folder", None))
        self.labelFilenameComments.setText(QCoreApplication.translate("CLS_Scan", u"Filename Comments", None))
        self.start.setText(QCoreApplication.translate("CLS_Scan", u"Start", None))
        self.fileLocationPath.setText(QCoreApplication.translate("CLS_Scan", u"File Location Path", None))
    # retranslateUi
    def start_acq(self):
        #if not self._daqActive:
        #self._daqActive = True
        print(self.frequency.value())
        self._daqOutput = signalOutput(outputChannel,1000000,iself.frequency.value())
        self._APD = APD_Reader(self.daqList.currentItem().text(),int(1000000/self.frequency.value()),continuous=False)
        #self._daqOutput.start_acq()
        pool = QThreadPool.globalInstance()
        
        self.worker = workerOutput(self._daqOutput)
        pool.start(self.worker)
        self._APD.start_acquisition()
        self._timer = QTimer()
        timing = (1/self.frequency.value())*1000
        self._timer.start(timing)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self.started = True
    def stop_acq(self):
        self.worker.terminateLoop()
        #if self._daqActive and self._started:
        #self._daq_active = False
        self._timer.stop()
        self._APD.stop_acquisition()
        self._APD.close_daq()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
    """     
    def value_change(self):
        if daq_active:
            self._daq_output.stop()
            self._daq_output.ao_channels.add_ao_voltage_chan(physical_channel=daq_channel,min_val = -10, max_val = 10) #at some point this should not be hardcoded
            self._daq_output.cfg_sample_clk_timing(rate =1000000,sample_mode= AcquisitionType.CONTINUOUS)
            self._test_writer = AnalogSingleChannelWriter(self._daq_output.out_stream, auto_start=True)
            time = np.linspace(0,1,1000000)
            self._samples = (((sawtooth(2*np.pi*self._frequency.value()*time,width=0.5))+1)/2)*self.amplitude.value()
            self._test_writer.write_many_samples(self._samples)
            self._daq_output.start()
            self._timer.stop()
            timing = (1/self.frequency.value())*1000*2
            self._timer.start(timing)
    """
    def write_graph(self):
        self.clsPlot.clear()
        self.clsPlot.plot(self._APD.read_values())
        self._APD.stop_acquisition()
        self._APD.start_acquisition()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    CLS_Scan = QMainWindow()
    ui = Ui_CLS_Scan()
    ui.setupUi(CLS_Scan)
    CLS_Scan.show()
    sys.exit(app.exec_())

