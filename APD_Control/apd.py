# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apdWduzLj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Thorlabs_APD import APD_Reader
import pyqtgraph as pg

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
        #All of these parts are set-up through the ui that is generated. If you would like to change them make sure to go change it through the ui file
        #You can change them in here to, designer just makes it really easy to do and visualize
        if not apdMonitor.objectName():
            apdMonitor.setObjectName(u"apdMonitor")
        apdMonitor.resize(726, 443)
        self.centralwidget = QWidget(apdMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.apd_graph = pg.PlotWidget(self.centralwidget) #this is the plotting widget, i replaced the Graphics view with it
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(QRect(40, 20, 461, 361))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(560, 270, 131, 41))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(560, 320, 131, 51))
        self.stop.setFont(font)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(560, 230, 131, 31))
        self.frequency.setFont(font)
        self.frequency.setMaximum(10000.000000000000000)
        self.frequency.setSingleStep(0.100000000000000)
        self.frequency.setValue(10.000000000000000)
        self.label_frequency = QLabel(self.centralwidget)
        self.label_frequency.setObjectName(u"label_frequency")
        self.label_frequency.setGeometry(QRect(560, 200, 131, 31))
        self.label_frequency.setFont(font)
        self.label_daqList = QLabel(self.centralwidget)
        self.label_daqList.setObjectName(u"label_daqList")
        self.label_daqList.setGeometry(QRect(560, 130, 131, 31))
        self.label_daqList.setFont(font)
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
        self.daqList.setGeometry(QRect(560, 160, 111, 31))
        self.daqList.setFont(font)
        self.daqList.setSortingEnabled(False)
        self.min_voltage = QDoubleSpinBox(self.centralwidget)
        self.min_voltage.setObjectName(u"min_voltage")
        self.min_voltage.setGeometry(QRect(560, 100, 131, 21))
        self.min_voltage.setMinimum(-10.000000000000000)
        self.min_voltage.setFont(font)
        self.label_min_voltage = QLabel(self.centralwidget)
        self.label_min_voltage.setObjectName(u"label_min_voltage")
        self.label_min_voltage.setGeometry(QRect(560, 75, 141, 21))
        self.label_min_voltage.setFont(font)
        self.label_max_voltage = QLabel(self.centralwidget)
        self.label_max_voltage.setObjectName(u"label_max_voltage")
        self.label_max_voltage.setGeometry(QRect(560, 25, 141, 21))
        self.label_max_voltage.setFont(font)
        self.max_voltage = QDoubleSpinBox(self.centralwidget)
        self.max_voltage.setObjectName(u"max_voltage")
        self.max_voltage.setGeometry(QRect(560, 50, 131, 21))
        self.max_voltage.setFont(font)
        self.max_voltage.setValue(10)
        apdMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(apdMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 726, 21))
        apdMonitor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(apdMonitor)
        self.statusbar.setObjectName(u"statusbar")
        apdMonitor.setStatusBar(self.statusbar)


        self.retranslateUi(apdMonitor)
        
        QMetaObject.connectSlotsByName(apdMonitor)
        #all of the rest of the code that I have added is below
        #If any changes are made to the ui, copy everything down
        #and only replace components above the top most comment
        #and replace the retranslateUI function.
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._apd = None
        self._timer = None
        self._active = False
        QMetaObject.connectSlotsByName(apdMonitor)
        self.frequency.valueChanged.connect(self.change_value)
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        self.daqList.currentItemChanged.connect(self.change_value)
        self.max_voltage.valueChanged.connect(self.change_value)
        self.min_voltage.valueChanged.connect(self.change_value)

    def retranslateUi(self, apdMonitor):
        apdMonitor.setWindowTitle(QCoreApplication.translate("apdMonitor", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("apdMonitor", u"Start", None))
        self.stop.setText(QCoreApplication.translate("apdMonitor", u"Stop", None))
        self.label_frequency.setText(QCoreApplication.translate("apdMonitor", u"Frequency", None))
        self.label_daqList.setText(QCoreApplication.translate("apdMonitor", u"DAQ Channel", None))

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

        self.label_min_voltage.setText(QCoreApplication.translate("apdMonitor", u"Minimum Voltage", None))
        self.label_max_voltage.setText(QCoreApplication.translate("apdMonitor", u"Maximum Voltage", None))

    #function for starting the acquisition 
    def start_acq(self):
        try:
            print(self.daqList.currentItem().text())
            self._apd = APD_Reader(self.daqList.currentItem().text(),int(1000000/(self.frequency.value()/2)),max_val = self.max_voltage.value(),min_val = self.min_voltage.value())
            self._apd.start_acquisition()
            self._timer = QTimer()
            time = (1/self.frequency.value())*1000
            self._timer.start(time)
            self._timer.timeout.connect(self.graph_values)
            self.start.setEnabled(False)
            self.stop.setEnabled(True)
            self._active = True
        except AttributeError:
            print("Make sure you selected a daq channel")
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
            self._apd = APD_Reader(self.daqList.currentItem().text(),int(1000000/(self.frequency.value()/2)),max_val = self.max_voltage.value(),min_val = self.min_voltage.value(),)
            self._apd.start_acquisition()
    #plots all of the values from the APD in the pyqtplot
    def graph_values(self):
        self.apd_graph.clear()
        self.apd_graph.plot(self._apd.read_values())

#Feel free to copy and paste the line below in other GUIs you make, just make sure to change names within it
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apdMonitor = QMainWindow()
    ui = Ui_apdMonitor()
    ui.setupUi(apdMonitor)
    apdMonitor.show()
    sys.exit(app.exec_())
    
