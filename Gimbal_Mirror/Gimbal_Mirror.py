# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gimbal_MirrorGJXRzR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Thorlabs_Motor.motor_control import Motor

class Ui_GimbalMirrors(object):
    def setupUi(self, GimbalMirrors):
        if not GimbalMirrors.objectName():
            GimbalMirrors.setObjectName(u"GimbalMirrors")
        GimbalMirrors.resize(465, 350)
        self.gimbalControl = QWidget(GimbalMirrors)
        self.gimbalControl.setObjectName(u"gimbalControl")
        self.x_axis = QSlider(self.gimbalControl)
        self.x_axis.setObjectName(u"x_axis")
        self.x_axis.setGeometry(QRect(60, 300, 341, 31))
        font = QFont()
        font.setPointSize(12)
        self.x_axis.setFont(font)
        self.x_axis.setMaximum(100000)
        self.x_axis.setOrientation(Qt.Horizontal)
        self.x_axis.setInvertedAppearance(False)
        self.x_axis.setInvertedControls(False)
        self.x_axis.setTickPosition(QSlider.TicksBelow)
        self.x_axis.setTickInterval(10000)
        self.y_axis = QSlider(self.gimbalControl)
        self.y_axis.setObjectName(u"y_axis")
        self.y_axis.setGeometry(QRect(20, 29, 31, 231))
        self.y_axis.setMaximum(100000)
        self.y_axis.setOrientation(Qt.Vertical)
        self.y_axis.setInvertedAppearance(True)
        self.y_axis.setInvertedControls(False)
        self.y_axis.setTickPosition(QSlider.TicksAbove)
        self.y_axis.setTickInterval(10000)
        self.camera_view = QGraphicsView(self.gimbalControl)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setGeometry(QRect(70, 20, 341, 261))
        GimbalMirrors.setCentralWidget(self.gimbalControl)
        self.menubar = QMenuBar(GimbalMirrors)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 465, 21))
        GimbalMirrors.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GimbalMirrors)
        self.statusbar.setObjectName(u"statusbar")
        GimbalMirrors.setStatusBar(self.statusbar)
        self._x_motor = Motor(27505032)
        self._y_motor = Motor(27004551)
        self.retranslateUi(GimbalMirrors)

        QMetaObject.connectSlotsByName(GimbalMirrors)
    # setupUi

    def retranslateUi(self, GimbalMirrors):
        GimbalMirrors.setWindowTitle(QCoreApplication.translate("GimbalMirrors", u"MainWindow", None))
    # retranslateUi
    def 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    GimbalMirrors = QMainWindow()
    ui = Ui_GimbalMirrors()
    ui.setupUi(GimbalMirrors)
    GimbalMirrors.show()
    sys.exit(app.exec_())
