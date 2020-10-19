# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CLS_ScanMpcKZV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import nidaqmx as daq
from Thorlabs_APD import APD_Reader
#Eventually I will read these values in and save them before exiting so this becomes unnecessary but thats a pipe dream as of now
initial_amplitude = 0.2
initial_frequency = 10
initial_offset = 0.200 #? I am not sure what this is supposed to be
initial_phase = 270
daq_channel = "Dev1/ao3"
#
class Ui_CLS_Scan(object):
    def setupUi(self, CLS_Scan):
        if not CLS_Scan.objectName():
            CLS_Scan.setObjectName(u"CLS_Scan")
        CLS_Scan.resize(1120, 870)
        self.centralwidget = QWidget(CLS_Scan)
        self.centralwidget.setObjectName(u"centralwidget")
        self.waveform_chart = QGraphicsView(self.centralwidget)
        self.waveform_chart.setObjectName(u"waveform_chart")
        self.waveform_chart.setGeometry(QRect(560, 350, 301, 211))
        self.l_t_graph_2 = QGraphicsView(self.centralwidget)
        self.l_t_graph_2.setObjectName(u"l_t_graph_2")
        self.l_t_graph_2.setGeometry(QRect(560, 590, 301, 211))
        self.waveform_chart_2 = QGraphicsView(self.centralwidget)
        self.waveform_chart_2.setObjectName(u"waveform_chart_2")
        self.waveform_chart_2.setGeometry(QRect(200, 350, 301, 211))
        self.l_t_graph = QGraphicsView(self.centralwidget)
        self.l_t_graph.setObjectName(u"l_t_graph")
        self.l_t_graph.setGeometry(QRect(200, 590, 301, 211))

        self.offset = QDoubleSpinBox(self.centralwidget)
        self.offset.setObjectName(u"offset")
        self.offset.setGeometry(QRect(450, 280, 62, 22))
        self.offset.setValue(initial_offset)
        self.phase = QDoubleSpinBox(self.centralwidget)
        self.phase.setObjectName(u"phase")
        self.phase.setGeometry(QRect(550, 280, 62, 22))
        self.phase.setMaximum(360)
        self.phase.setValue(initial_phase)
        self.amplitude = QDoubleSpinBox(self.centralwidget)
        self.amplitude.setObjectName(u"amplitude")
        self.amplitude.setGeometry(QRect(450, 230, 62, 22))
        self.amplitude.setValue(initial_amplitude)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(550, 230, 62, 22))
        self.frequency.setMaximum(10000)
        self.frequency.setValue(initial_frequency)
        self.label_amplitude = QLabel(self.centralwidget)
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(620, 170, 62, 22))
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(740, 210, 111, 51))
        self.capture = QPushButton(self.centralwidget)
        self.capture.setObjectName(u"capture")
        self.capture.setGeometry(QRect(740, 280, 111, 51))
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(200, 170, 201, 31))
        self.daq_channel = QTextEdit(self.centralwidget)
        self.daq_channel.setObjectName(u"daq_channel")
        self.daq_channel.setGeometry(QRect(200, 240, 111, 31))
        self.single_channel_m = QDoubleSpinBox(self.centralwidget)
        self.single_channel_m.setObjectName(u"single_channel_m")
        self.single_channel_m.setGeometry(QRect(200, 300, 62, 22))
        self.single_channel_m_2 = QDoubleSpinBox(self.centralwidget)
        self.single_channel_m_2.setObjectName(u"single_channel_m_2")
        self.single_channel_m_2.setGeometry(QRect(330, 300, 62, 22))
        self.cavity = QTextEdit(self.centralwidget)
        self.cavity.setObjectName(u"cavity")
        self.cavity.setGeometry(QRect(420, 170, 161, 31))
        self.saving_folder = QPlainTextEdit(self.centralwidget)
        self.saving_folder.setObjectName(u"saving_folder")
        self.saving_folder.setGeometry(QRect(200, 106, 661, 31))
        self.filename_comments = QPlainTextEdit(self.centralwidget)
        self.filename_comments.setObjectName(u"filename_comments")
        self.filename_comments.setGeometry(QRect(700, 170, 161, 31))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(620, 210, 111, 51))
        CLS_Scan.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CLS_Scan)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 26))
        CLS_Scan.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CLS_Scan)
        self.statusbar.setObjectName(u"statusbar")
        CLS_Scan.setStatusBar(self.statusbar)
        
        #Just a laundry list of labels
        self.label_waveform_chart = QLabel(self.centralwidget)
        self.label_waveform_chart.setObjectName(u"label_waveform_chart")
        self.label_waveform_chart.setGeometry(QRect(560, 330, 191, 16))
        self.label_l_t_graph_2 = QLabel(self.centralwidget)
        self.label_l_t_graph_2.setObjectName(u"label_l_t_graph_2")
        self.label_l_t_graph_2.setGeometry(QRect(560, 570, 111, 16))
        self.label_l_t_graph = QLabel(self.centralwidget)
        self.label_l_t_graph.setObjectName(u"label_l_t_graph")
        self.label_l_t_graph.setGeometry(QRect(200, 570, 111, 16))
        self.label_waveform_chart_2 = QLabel(self.centralwidget)
        self.label_waveform_chart_2.setObjectName(u"label_waveform_chart_2")
        self.label_waveform_chart_2.setGeometry(QRect(200, 330, 191, 16))
        self.label_amplitude.setObjectName(u"label_amplitude")
        self.label_amplitude.setGeometry(QRect(450, 210, 71, 16))
        self.label_frequency = QLabel(self.centralwidget)
        self.label_frequency.setObjectName(u"label_frequency")
        self.label_frequency.setGeometry(QRect(550, 210, 71, 16))
        self.label_offset = QLabel(self.centralwidget)
        self.label_offset.setObjectName(u"label_offset")
        self.label_offset.setGeometry(QRect(450, 260, 71, 16))
        self.label_phase = QLabel(self.centralwidget)
        self.label_phase.setObjectName(u"label_phase")
        self.label_phase.setGeometry(QRect(550, 260, 71, 16))
        self.label_wait_time = QLabel(self.centralwidget)
        self.label_wait_time.setObjectName(u"label_wait_time")
        self.label_wait_time.setGeometry(QRect(620, 150, 71, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 150, 101, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 150, 55, 16))
        self.label_saving_folder = QLabel(self.centralwidget)
        self.label_saving_folder.setObjectName(u"label_saving_folder")
        self.label_saving_folder.setGeometry(QRect(200, 80, 181, 16))
        self.label_single_channel_m = QLabel(self.centralwidget)
        self.label_single_channel_m.setObjectName(u"label_single_channel_m")
        self.label_single_channel_m.setGeometry(QRect(200, 280, 111, 16))
        self.label_single_channel_m_2 = QLabel(self.centralwidget)
        self.label_single_channel_m_2.setObjectName(u"label_single_channel_m_2")
        self.label_single_channel_m_2.setGeometry(QRect(330, 280, 111, 16))
        self.label_filename_comments = QLabel(self.centralwidget)
        self.label_filename_comments.setObjectName(u"label_filename_comments")
        self.label_filename_comments.setGeometry(QRect(700, 150, 131, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 220, 111, 16))
        #This is where the labels end        
        self.retranslateUi(CLS_Scan)
        self._daq_output = None
        self._APD = None
        self._daq_active = False
        self._started = False

        QMetaObject.connectSlotsByName(CLS_Scan)
        
        #this will be where all of my code will go
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        self.frequency.valueChanged.connect(self.value_change)
        self.amplitude.valueChanged.connect(self.value_change)
        self.offset.valueChanged.connect(self.value_change)
        

    # setupUi

    def retranslateUi(self, CLS_Scan):
        CLS_Scan.setWindowTitle(QCoreApplication.translate("CLS_Scan", u"MainWindow", None))
        self.label_waveform_chart.setText(QCoreApplication.translate("CLS_Scan", u"Waveform Chart 2", None))
        self.label_l_t_graph_2.setText(QCoreApplication.translate("CLS_Scan", u"L-T Graph 2", None))
        self.label_l_t_graph.setText(QCoreApplication.translate("CLS_Scan", u"L-T Graph", None))
        self.label_waveform_chart_2.setText(QCoreApplication.translate("CLS_Scan", u"Waveform Chart", None))
        self.label_amplitude.setText(QCoreApplication.translate("CLS_Scan", u"Amplitude", None))
        self.label_frequency.setText(QCoreApplication.translate("CLS_Scan", u"Frequency", None))
        self.label_offset.setText(QCoreApplication.translate("CLS_Scan", u"Offset", None))
        self.label_phase.setText(QCoreApplication.translate("CLS_Scan", u"Phase", None))
        self.label_wait_time.setText(QCoreApplication.translate("CLS_Scan", u"Wait Time", None))
        self.stop.setText(QCoreApplication.translate("CLS_Scan", u"Stop", None))
        self.capture.setText(QCoreApplication.translate("CLS_Scan", u"Capture", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("CLS_Scan", u"Brandon Mehlenbacher", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("CLS_Scan", u"Ceci", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("CLS_Scan", u"Beau", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("CLS_Scan", u"Lisa-Maria", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("CLS_Scan", u"Who Are you", None))
        self.label_2.setText(QCoreApplication.translate("CLS_Scan", u"Cavity", None))
        self.label_3.setText(QCoreApplication.translate("CLS_Scan", u"DAQ Channel", None))
        self.label_single_channel_m.setText(QCoreApplication.translate("CLS_Scan", u"Single Channel M", None))
        self.label_single_channel_m_2.setText(QCoreApplication.translate("CLS_Scan", u"Single Channel M", None))
        self.label_saving_folder.setText(QCoreApplication.translate("CLS_Scan", u"Saving Folder", None))
        self.label_filename_comments.setText(QCoreApplication.translate("CLS_Scan", u"Filename Comments", None))
        self.start.setText(QCoreApplication.translate("CLS_Scan", u"Start", None))
    # retranslateUi
    def start_acq(self):
        if not self._daq_active:
            self._daq_active = True
            self._daq_output = daq.Task()
            self._daq_output.ao_channels.add_ao_func_gen_chan(physical_channel=daq_channel,type=daq.constants.FuncGenType.TRIANGLE,freq = self.frequency.value(),amplitude = self.amplitude.value(),offset = self.offset.value()) #at some point this should not be hardcoded
            self._APD = APD_Reader(self.daq_channel.Value(),1000000/self.frequency.value())
            self._daq_output.start()
            self._APD.start_acquisition()
            self.started = True
    def stop_acq(self):
        if self._daq_active and self._started:
            self._daq_active = False
            self._daq_output.stop()
            self._daq_output.close()
            self._APD.stop_acquisition()
            self._APD.close_daq()
            
    def value_change(self):
        if daq_active:
            self._daq_output.stop()
            self._daq_ouput.ao_channels.add_ao_func_gen_chan(daq_channel,type=daq.constants.FuncGenType.TRIANGLE,freq = self.frequency.value(),amplitude = self.amplitude.value(),offset = self.offset.value())
            self._daq_output.start()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    CLS_Scan = QMainWindow()
    ui = Ui_CLS_Scan()
    ui.setupUi(CLS_Scan)
    CLS_Scan.show()
    sys.exit(app.exec_())

