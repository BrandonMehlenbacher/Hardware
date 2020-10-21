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
    
    simple description of how to run this program,
    Exec: Exec ./apd.py from the command line or powershell to initialize the program
    Run: Click the 

    """
    def setupUi(self, apdMonitor):
        if not apdMonitor.objectName():
            apdMonitor.setObjectName(u"apdMonitor")
        apdMonitor.resize(726, 443)
        self.centralwidget = QWidget(apdMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        #self.apd_graph = QGraphicsView(self.centralwidget)
        self.apd_graph = pg.PlotWidget(self.centralwidget)
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(QRect(40, 20, 461, 361))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(560, 190, 131, 71))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(560, 300, 131, 71))
        self.stop.setFont(font)
        self.frequency = QDoubleSpinBox(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(560, 140, 131, 31))
        self.frequency.setFont(font)
        self.frequency.setMaximum(10000.000000000000000)
        self.frequency.setSingleStep(0.100000000000000)
        self.frequency.setValue(10.000000000000000)
        self.label_frequency = QLabel(self.centralwidget)
        self.label_frequency.setObjectName(u"label_frequency")
        self.label_frequency.setGeometry(QRect(560, 100, 131, 31))
        self.label_frequency.setFont(font)
        self.label_daqList = QLabel(self.centralwidget)
        self.label_daqList.setObjectName(u"label_daqList")
        self.label_daqList.setGeometry(QRect(560, 20, 131, 31))
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
        self.daqList.setGeometry(QRect(560, 60, 111, 31))
        self.daqList.setSortingEnabled(False)
        apdMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(apdMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 726, 26))
        apdMonitor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(apdMonitor)
        self.statusbar.setObjectName(u"statusbar")
        apdMonitor.setStatusBar(self.statusbar)

        self.retranslateUi(apdMonitor)

        QMetaObject.connectSlotsByName(apdMonitor)
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
        
    # setupUi

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

    # retranslateUi

    def start_acq(self):
        print(self.daqList.currentItem().text())
        self._apd = APD_Reader(self.daqList.currentItem().text(),int(1000000/(self.frequency.value()/2)))
        self._apd.start_acquisition()
        self._timer = QTimer()
        time = (1/self.frequency.value())*1000
        self._timer.start(time)
        self._timer.timeout.connect(self.graph_values)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self._active = True
    def stop_acq(self):
        self._apd.stop_acquisition()
        self._apd.close_daq()
        self._apd = None
        self._timer.stop()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._active = False
    def change_value(self):
        if self._active:
            self._apd.stop_acquisition()
            self._apd.close_daq()
            self._apd = None
            self._apd = APD_Reader(self.daqList.currentItem().text(),int(1000000/(self.frequency.value()/2)))
            self._apd.start_acquisition()
    def graph_values(self):
        self.apd_graph.clear()
        self.apd_graph.plot(self._apd.read_values())
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apdMonitor = QMainWindow()
    ui = Ui_apdMonitor()
    ui.setupUi(apdMonitor)
    apdMonitor.show()
    sys.exit(app.exec_())
