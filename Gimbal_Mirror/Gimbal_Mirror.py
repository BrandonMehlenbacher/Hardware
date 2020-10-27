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
import pyqtgraph as pg
import thorlabs_apt as apt
from instrumental import instrument, list_instruments
from motor_control import Motor



class Ui_GimbalMirrors(object):
    def setupUi(self, GimbalMirrors):
        if not GimbalMirrors.objectName():
            GimbalMirrors.setObjectName(u"GimbalMirrors")
        GimbalMirrors.resize(571, 386)
        self.gimbalControl = QWidget(GimbalMirrors)
        self.gimbalControl.setObjectName(u"gimbalControl")
        self.x_axis = QSlider(self.gimbalControl)
        self.x_axis.setObjectName(u"x_axis")
        self.x_axis.setGeometry(QRect(70, 300, 341, 31))
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
        self.y_axis.setGeometry(QRect(20, 40, 31, 231))
        self.y_axis.setMaximum(100000)
        self.y_axis.setOrientation(Qt.Vertical)
        self.y_axis.setInvertedAppearance(True)
        self.y_axis.setInvertedControls(False)
        self.y_axis.setTickPosition(QSlider.TicksAbove)
        self.y_axis.setTickInterval(10000)
        #self.camera_view = QGraphicsView(self.gimbalControl)
        self.camera_view = pg.ImageView()
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setGeometry(QRect(70, 20, 341, 261))
        self.label_y_axis = QLabel(self.gimbalControl)
        self.label_y_axis.setObjectName(u"label_y_axis")
        self.label_y_axis.setGeometry(QRect(10, 20, 47, 13))
        self.label_y_axis.setFont(font)
        self.label_x_axis = QLabel(self.gimbalControl)
        self.label_x_axis.setObjectName(u"label_x_axis")
        self.label_x_axis.setGeometry(QRect(10, 310, 47, 13))
        self.label_x_axis.setFont(font)
        self.start = QPushButton(self.gimbalControl)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(430, 60, 111, 51))
        self.start.setFont(font)
        self.stop = QPushButton(self.gimbalControl)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(430, 180, 111, 51))
        self.stop.setFont(font)
        GimbalMirrors.setCentralWidget(self.gimbalControl)
        self.menubar = QMenuBar(GimbalMirrors)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 21))
        GimbalMirrors.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GimbalMirrors)
        self.statusbar.setObjectName(u"statusbar")
        GimbalMirrors.setStatusBar(self.statusbar)

        self.retranslateUi(GimbalMirrors)

        QMetaObject.connectSlotsByName(GimbalMirrors)
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self._instrument_list = list_instruments()
        self._list_devices = apt.list_available_devices()
        self._timer = None
        self._x_motor = None
        self._y_motor = None
        self._camera = None
        self._first_start = True
    # setupUi
     def retranslateUi(self, GimbalMirrors):
        GimbalMirrors.setWindowTitle(QCoreApplication.translate("GimbalMirrors", u"MainWindow", None))
        self.label_y_axis.setText(QCoreApplication.translate("GimbalMirrors", u"Y-Axis", None))
        self.label_x_axis.setText(QCoreApplication.translate("GimbalMirrors", u"X-Axis", None))
        self.pushButton.setText(QCoreApplication.translate("GimbalMirrors", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("GimbalMirrors", u"Stop", None))
    # retranslateUi

    def change_x_axis(self):
        x_axis_value = self.x_axis.value()/10000
        self._x_motor.move_absolute(x_axis_value)
    def change_y_axis(self):
        y_axis_value = self.x_axis.value()/10000
        self._y_motor.move_absolute(y_axis_value)
    def start(self):
        
        if self._first_start:
            self._x_motor = Motor(self._list_devices[0][1])
            self._y_motor = Motor(self._list_devices[1][1])
            for x in range(len(self._instrument_list)):
                if self._instrument_list[x]['serial'] == b'4102906167':
                    self._camera = instrument(self._instrument_list[x])
                    break
            if (self._camer == None):
                print("There was an error intializing the camera, please go fix it")
                QCoreApplication.quit()
            self._camera.start_live_video()
            self._timer = QTimer()
            self._timer.start(10) #10 ms before showing next frame
            self._timer.timeout.connect(self.view_camera)
            self._first_start = True
        else:
            self._x_motor.enable()
            self._y_motor.enable()
            self._camera.start_live_video()
            self._timer = QTimer()
            self._timer.start(10) #10 ms before showing next frame
            self._timer.timeout.connect(self.view_camera)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
    def stop(self):
        self._x_motor.disable()
        self._y_motor.disable()
        self._timer = QTimer()
        self._timer.stop()
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
    def view_camera(self):
        self.camera_view.image(self._camera.latest_frame())
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    GimbalMirrors = QMainWindow()
    ui = Ui_GimbalMirrors()
    ui.setupUi(GimbalMirrors)
    GimbalMirrors.show()
    sys.exit(app.exec_())
