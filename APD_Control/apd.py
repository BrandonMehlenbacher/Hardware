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


class Ui_apdMonitor(object):
    def setupUi(self, apdMonitor):
        if not apdMonitor.objectName():
            apdMonitor.setObjectName(u"apdMonitor")
        apdMonitor.resize(654, 418)
        self.centralwidget = QWidget(apdMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.apd_graph = QGraphicsView(self.centralwidget)
        self.apd_graph.setObjectName(u"apd_graph")
        self.apd_graph.setGeometry(QRect(10, 10, 461, 361))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(490, 70, 131, 71))
        font = QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(490, 220, 131, 71))
        self.stop.setFont(font)
        apdMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(apdMonitor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 654, 21))
        apdMonitor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(apdMonitor)
        self.statusbar.setObjectName(u"statusbar")
        apdMonitor.setStatusBar(self.statusbar)
        self.start.btnEnabled(True)
        self.stop.btnEnabled(False)
        self.retranslateUi(apdMonitor)

        QMetaObject.connectSlotsByName(apdMonitor)
    # setupUi

    def retranslateUi(self, apdMonitor):
        apdMonitor.setWindowTitle(QCoreApplication.translate("apdMonitor", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("apdMonitor", u"Start", None))
        self.stop.setText(QCoreApplication.translate("apdMonitor", u"Stop", None))
    # retranslateUi
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apdMonitor = QMainWindow()
    ui = Ui_apdMonitor()
    ui.setupUi(apdMonitor)
    apdMonitor.show()
    sys.exit(app.exec_())
