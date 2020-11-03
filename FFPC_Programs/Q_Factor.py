# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apdWduzLj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import pandas as pd
sys.path.append(r"C:\Users\Goldsmith\Desktop\Hardware") #this adds a path to the hardware directory so I have access to all of the different packages I make

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from APD_Control.Thorlabs_APD import APD_Reader
from Q_Calc import QFactor
import scipy.optimize as optimize
import numpy as np
import pyqtgraph as pg

class Ui_QMonitor(object):
    def setupUi(self, QMonitor):
        if not QMonitor.objectName():
            QMonitor.setObjectName(u"QMonitor")
        QMonitor.resize(945, 453)
        self.centralwidget = QWidget(QMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        #self.apd_graph = QGraphicsView(self.centralwidget)
        self.apd_graph = pg.PlotWidget(self.centralwidget)
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(QRect(40, 20, 461, 361))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(750, 120, 131, 51))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(750, 200, 131, 51))
        self.stop.setFont(font)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(750, 70, 131, 31))
        self.frequency.setFont(font)
        self.frequency.setMaximum(10000.000000000000000)
        self.frequency.setSingleStep(0.100000000000000)
        self.frequency.setValue(10.000000000000000)
        self.label_frequency = QLabel(self.centralwidget)
        self.label_frequency.setObjectName(u"label_frequency")
        self.label_frequency.setGeometry(QRect(750, 40, 131, 31))
        self.label_frequency.setFont(font)
        self.label_daqList = QLabel(self.centralwidget)
        self.label_daqList.setObjectName(u"label_daqList")
        self.label_daqList.setGeometry(QRect(560, 180, 131, 31))
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
        self.daqList.setGeometry(QRect(560, 220, 111, 31))
        self.daqList.setFont(font)
        self.daqList.setSortingEnabled(False)
        self.min_voltage = QDoubleSpinBox(self.centralwidget)
        self.min_voltage.setObjectName(u"min_voltage")
        self.min_voltage.setGeometry(QRect(560, 140, 131, 31))
        self.min_voltage.setMinimum(-10.000000000000000)
        self.min_voltage.setFont(font)
        self.label_max_voltage_2 = QLabel(self.centralwidget)
        self.label_max_voltage_2.setObjectName(u"label_max_voltage_2")
        self.label_max_voltage_2.setGeometry(QRect(560, 110, 171, 31))
        self.label_max_voltage_2.setFont(font)
        self.label_max_voltage = QLabel(self.centralwidget)
        self.label_max_voltage.setObjectName(u"label_max_voltage")
        self.label_max_voltage.setGeometry(QRect(560, 40, 171, 31))
        self.label_max_voltage.setFont(font)
        self.max_voltage = QDoubleSpinBox(self.centralwidget)
        self.max_voltage.setObjectName(u"max_voltage")
        self.max_voltage.setGeometry(QRect(560, 70, 131, 31))
        self.max_voltage.setValue(10.000000000000000)
        self.max_voltage.setFont(font)
        self.Value_Q_Factor = QLCDNumber(self.centralwidget)
        self.Value_Q_Factor.setObjectName(u"Value_Q_Factor")
        self.Value_Q_Factor.setGeometry(QRect(740, 290, 131, 51))
        self.Push_Q_Factor = QPushButton(self.centralwidget)
        self.Push_Q_Factor.setObjectName(u"Push_Q_Factor")
        self.Push_Q_Factor.setGeometry(QRect(560, 290, 121, 51))
        self.Push_Q_Factor.setFont(font)
        self.label_q_factor = QLabel(self.centralwidget)
        self.label_q_factor.setObjectName(u"label_q_factor")
        self.label_q_factor.setGeometry(QRect(740, 260, 131, 31))
        self.label_q_factor.setFont(font)
        QMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 945, 26))
        QMonitor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QMonitor)
        self.statusbar.setObjectName(u"statusbar")
        QMonitor.setStatusBar(self.statusbar)

        self.retranslateUi(QMonitor)

        QMetaObject.connectSlotsByName(QMonitor)
        #all of the rest of the code that I have added is below
        #If any changes are made to the ui, copy everything down
        #and only replace components above the top most comment
        #and replace the retranslateUI function.
        self._filename = "qFactorCavity_0509_planarSubstrate.csv" # this will later be part of the GUI but not today 11/03/2020
        self.start.setEnabled(True)
        self.stop.setEnabled(True)
        self._apd = None
        self._timer = None
        self._active = False
        self._QCalc = None
        self._sweepFreq = 40 #hardcoding for now will come back later
        self._resolution = 1000000 #hardcoding for now will come back later
        self._correction = int(self._resolution/self._sweepFreq)
        self._x_values = (120.5/self._correction)*np.array(range(self._correction))
        QMetaObject.connectSlotsByName(QMonitor)
        self.frequency.valueChanged.connect(self.change_value)
        self.start.clicked.connect(self.start_acq)
        self.stop.clicked.connect(self.stop_acq)
        self.daqList.currentItemChanged.connect(self.change_value)
        self.max_voltage.valueChanged.connect(self.change_value)
        self.min_voltage.valueChanged.connect(self.change_value)
        self.Push_Q_Factor.clicked.connect(self.qFactor)

    def retranslateUi(self, QMonitor):
        QMonitor.setWindowTitle(QCoreApplication.translate("QMonitor", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("QMonitor", u"Start", None))
        self.stop.setText(QCoreApplication.translate("QMonitor", u"Stop", None))
        self.label_frequency.setText(QCoreApplication.translate("QMonitor", u"Frequency", None))
        self.label_daqList.setText(QCoreApplication.translate("QMonitor", u"DAQ Channel", None))

        __sortingEnabled = self.daqList.isSortingEnabled()
        self.daqList.setSortingEnabled(False)
        ___qlistwidgetitem = self.daqList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai0", None));
        ___qlistwidgetitem1 = self.daqList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai1", None));
        ___qlistwidgetitem2 = self.daqList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai2", None));
        ___qlistwidgetitem3 = self.daqList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai3", None));
        ___qlistwidgetitem4 = self.daqList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai4", None));
        ___qlistwidgetitem5 = self.daqList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai5", None));
        ___qlistwidgetitem6 = self.daqList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai6", None));
        ___qlistwidgetitem7 = self.daqList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai7", None));
        ___qlistwidgetitem8 = self.daqList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("QMonitor", u"Dev1/ai8", None));
        self.daqList.setSortingEnabled(__sortingEnabled)

        self.label_max_voltage_2.setText(QCoreApplication.translate("QMonitor", u"Minimum Voltage", None))
        self.label_max_voltage.setText(QCoreApplication.translate("QMonitor", u"Maximum Voltage", None))
        self.Push_Q_Factor.setText(QCoreApplication.translate("QMonitor", u"Q-Factor", None))
        self.label_q_factor.setText(QCoreApplication.translate("QMonitor", u"Q-Factor", None))

    #function for starting the acquisition 
    def start_acq(self):
        try:
            if self._active:
                self._apd.start_acquisition()
            else:
                print(self.daqList.currentItem().text())
                self._apd = APD_Reader(self.daqList.currentItem().text(),int(self._correction),max_val = self.max_voltage.value(),min_val = self.min_voltage.value(),continuous=False)
                self._apd.start_acquisition()
                self._timer = QTimer()
                self._active = True
        except AttributeError:
            print("Make sure you selected a daq channel")
    #function for stopping the acquisition
    def stop_acq(self):
        if self._active:
            self._apd.close_daq()
            self._apd = None
            self._active = False
    #if any of the values have changed, everything gets reset if the DAQ is actually active, if not ignores it
    def change_value(self):
        if self._active:
            self._apd.stop_acquisition()
            self._apd.close_daq()
            self._apd = None
            self._apd = APD_Reader(self.daqList.currentItem().text(),int(self._correction),max_val = self.max_voltage.value(),min_val = self.min_voltage.value(),)
            self._apd.start_acquisition()
    #plots all of the values from the APD in the pyqtplot
    def qFactor(self):
        if self._active:
            self.apd_graph.clear()
            values = self._apd.read_values()
            x_values = self._x_values[0:int(len(self._x_values)/2)]
            y_values = values[0:int(len(self._x_values)/2)]
            dataframe = pd.DataFrame({'x_values':x_values,'y_values':y_values})
            self.apd_graph.plot(x_values,y_values)
            self._QCalc = QFactor(x_values,y_values)
            self._QCalc.fitLorentz()
            sigma = self._QCalc.getSigma()
            center = self._QCalc.getCenter()
            amplitude = self._QCalc.getAmplitude()
            self._apd.stop_acquisition()
            self.Value_Q_Factor.display(780000/sigma)
            newYValues = self._QCalc.getNewYVal()
            self.apd_graph.plot(x_values,newYValues)
            dataframe.to_csv(self._filename)
            
        
#Feel free to copy and paste the line below in other GUIs you make, just make sure to change names within it
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    QMonitor = QMainWindow()
    ui = Ui_QMonitor()
    ui.setupUi(QMonitor)
    QMonitor.show()
    sys.exit(app.exec_())
    
