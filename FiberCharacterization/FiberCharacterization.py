# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FiberCharacterizationQpvcyo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import warnings
import time
from datetime import date
import os
warnings.simplefilter("ignore")
sys.path.append("C:/Users/bmehl/Desktop/Research_Programs/Hardware")


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from instrumental import instrument, list_instruments
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from ECC100.ecc100_control import ECC100Control

class Ui_FiberCharacterization(object):
    def __init__(self):
        self.instrumentList = list_instruments()
        self.camera = self.connect_to_camera(b'4103577042')
        self.timeBetweenFrames = 50
        self.live = False
        self.today = str(date.today())
        self.parentPath = "//marlin.chem.wisc.edu/groups/Goldsmith Group/X/dataBackup/Data/ELN_Data"
        self.axis = 1 # this is the axis needed for taking the pictures, can be changed if necessary
        self.ecc = ECC100Control()
        self.ecc.connect()
        self.ecc.set_frequency(self.axis,100000)
        self.ecc.set_amplitude(self.axis,30000)
    def setupUi(self, FiberCharacterization):
        if not FiberCharacterization.objectName():
            FiberCharacterization.setObjectName(u"FiberCharacterization")
        FiberCharacterization.resize(942, 753)
        self.centralwidget = QWidget(FiberCharacterization)
        self.centralwidget.setObjectName(u"centralwidget")
        self.capture = QPushButton(self.centralwidget)
        self.capture.setObjectName(u"capture")
        self.capture.setGeometry(QRect(20, 270, 191, 41))
        font = QFont()
        font.setPointSize(12)
        self.capture.setFont(font)
        self.stepSize = QDoubleSpinBox(self.centralwidget)
        self.stepSize.setObjectName(u"stepSize")
        self.stepSize.setGeometry(QRect(20, 360, 191, 31))
        self.stepSize.setFont(font)
        self.stepSize.setMaximum(1000.000000000000000)
        self.stepSize.setValue(128.000000000000000)
        self.labelStepSize = QLabel(self.centralwidget)
        self.labelStepSize.setObjectName(u"labelStepSize")
        self.labelStepSize.setGeometry(QRect(20, 330, 151, 21))
        self.labelStepSize.setFont(font)
        self.cameraImage = pg.ImageView()
        self.cameraImage.setObjectName(u"cameraImage")
        self.cameraImage.setGeometry(QRect(260, 160, 601, 471))
        self.cameraImage.show()
        self.filepath = QLineEdit(self.centralwidget)
        self.filepath.setObjectName(u"filepath")
        self.filepath.setGeometry(QRect(20, 70, 841, 31))
        self.labelFilepath = QLabel(self.centralwidget)
        self.labelFilepath.setObjectName(u"labelFilepath")
        self.labelFilepath.setGeometry(QRect(20, 40, 121, 31))
        self.labelFilepath.setFont(font)
        self.users = QListWidget(self.centralwidget)
        QListWidgetItem(self.users)
        QListWidgetItem(self.users)
        QListWidgetItem(self.users)
        QListWidgetItem(self.users)
        QListWidgetItem(self.users)
        self.users.setObjectName(u"users")
        self.users.setGeometry(QRect(20, 160, 191, 31))
        self.labelUsers = QLabel(self.centralwidget)
        self.labelUsers.setObjectName(u"labelUsers")
        self.labelUsers.setGeometry(QRect(20, 130, 55, 16))
        self.labelUsers.setFont(font)
        self.live = QPushButton(self.centralwidget)
        self.live.setObjectName(u"live")
        self.live.setGeometry(QRect(20, 210, 191, 41))
        self.live.setFont(font)
        self.labelExposure = QLabel(self.centralwidget)
        self.labelExposure.setObjectName(u"labelExposure")
        self.labelExposure.setGeometry(QRect(20, 400, 211, 41))
        self.labelExposure.setFont(font)
        self.exposureTime = QDoubleSpinBox(self.centralwidget)
        self.exposureTime.setObjectName(u"exposureTime")
        self.exposureTime.setGeometry(QRect(20, 440, 191, 31))
        self.exposureTime.setFont(font)
        self.exposureTime.setValue(20.000000000000000)
        self.lableAverageNumber = QLabel(self.centralwidget)
        self.lableAverageNumber.setObjectName(u"lableAverageNumber")
        self.lableAverageNumber.setGeometry(QRect(20, 480, 181, 21))
        self.lableAverageNumber.setFont(font)
        self.labelDelayTime = QLabel(self.centralwidget)
        self.labelDelayTime.setObjectName(u"labelDelayTime")
        self.labelDelayTime.setGeometry(QRect(20, 550, 231, 51))
        self.labelDelayTime.setFont(font)
        self.labelDelayTime.setWordWrap(True)
        self.delayTime = QDoubleSpinBox(self.centralwidget)
        self.delayTime.setObjectName(u"delayTime")
        self.delayTime.setGeometry(QRect(20, 600, 191, 31))
        self.delayTime.setFont(font)
        self.delayTime.setMaximum(10000.000000000000000)
        self.delayTime.setValue(0.000000000000000)
        self.averageNumber = QSpinBox(self.centralwidget)
        self.averageNumber.setObjectName(u"averageNumber")
        self.averageNumber.setGeometry(QRect(20, 510, 191, 31))
        self.averageNumber.setFont(font)
        self.averageNumber.setValue(3)
        self.moveBy = QDoubleSpinBox(self.centralwidget)
        self.moveBy.setObjectName(u"moveTo")
        self.moveBy.setGeometry(QRect(20, 660, 191, 31))
        self.moveBy.setFont(font)
        self.moveBy.setMinimum(-12500.000000000000000)
        self.moveBy.setMaximum(25000.000000000000000)
        self.moveBy.setSingleStep(0.001000000000000)
        self.moveBy.setValue(0.000000000000000)
        self.moveBy.setKeyboardTracking(False)
        self.labelMoveTo = QLabel(self.centralwidget)
        self.labelMoveTo.setObjectName(u"labelMoveTo")
        self.labelMoveTo.setGeometry(QRect(20, 640, 141, 16))
        self.labelMoveTo.setFont(font)
        self.fiberNumber = QSpinBox(self.centralwidget)
        self.fiberNumber.setObjectName(u"fiberNumber")
        self.fiberNumber.setGeometry(QRect(260, 160, 191, 31))
        self.fiberNumber.setFont(font)
        self.labelFiberNumber = QLabel(self.centralwidget)
        self.labelFiberNumber.setObjectName(u"labelFiberNumber")
        self.labelFiberNumber.setGeometry(QRect(260, 130, 161, 16))
        self.labelFiberNumber.setFont(font)
        self.folderName = QTextEdit(self.centralwidget)
        self.folderName.setObjectName(u"folderName")
        self.folderName.setGeometry(QRect(480, 160, 191, 41))
        self.background = QCheckBox(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(680, 170, 251, 31))
        self.background.setFont(font)
        self.background.setChecked(False)
        self.labelFolderName = QLabel(self.centralwidget)
        self.labelFolderName.setObjectName(u"labelFolderName")
        self.labelFolderName.setGeometry(QRect(480, 130, 141, 16))
        self.labelFolderName.setFont(font)
        FiberCharacterization.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FiberCharacterization)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 942, 26))
        FiberCharacterization.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FiberCharacterization)
        self.statusbar.setObjectName(u"statusbar")
        FiberCharacterization.setStatusBar(self.statusbar)

        self.retranslateUi(FiberCharacterization)

        self.users.setCurrentRow(0)

        self.filepath = self.parentPath+'/'+self.users.currentItem().text()+'/'+self.folderName.toPlainText()+'/'+self.today

        QMetaObject.connectSlotsByName(FiberCharacterization)
        self.live.clicked.connect(self.start_video)
        self.capture.clicked.connect(self.capture_image)
        self.moveBy.valueChanged.connect(self.move_attocube)
        self.users.currentItemChanged.connect(self.change_filepath)
        self.timer = QTimer()
    # setupUi

    def retranslateUi(self, FiberCharacterization):
        FiberCharacterization.setWindowTitle(QCoreApplication.translate("FiberCharacterization", u"MainWindow", None))
        self.capture.setText(QCoreApplication.translate("FiberCharacterization", u"Capture", None))
        self.labelStepSize.setText(QCoreApplication.translate("FiberCharacterization", u"Step Size (nm)", None))
        self.labelFilepath.setText(QCoreApplication.translate("FiberCharacterization", u"Filepath", None))

        __sortingEnabled = self.users.isSortingEnabled()
        self.users.setSortingEnabled(False)
        ___qlistwidgetitem = self.users.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("FiberCharacterization", u"Beau Schweitzer", None));
        ___qlistwidgetitem1 = self.users.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("FiberCharacterization", u"Alex Fairhall", None));
        ___qlistwidgetitem2 = self.users.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("FiberCharacterization", u"Brandon Mehlenbacher", None));
        ___qlistwidgetitem3 = self.users.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("FiberCharacterization", u"Lisa-Maria Needham", None));
        ___qlistwidgetitem4 = self.users.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("FiberCharacterization", u"Julia Rasch", None));
        self.users.setSortingEnabled(__sortingEnabled)

        self.labelUsers.setText(QCoreApplication.translate("FiberCharacterization", u"Users", None))
        self.live.setText(QCoreApplication.translate("FiberCharacterization", u"Live", None))
        self.labelExposure.setText(QCoreApplication.translate("FiberCharacterization", u"Exposure Time (ms)", None))
        self.lableAverageNumber.setText(QCoreApplication.translate("FiberCharacterization", u"Average Number", None))
        self.labelDelayTime.setText(QCoreApplication.translate("FiberCharacterization", u"Delay Time Between Frames (ms)", None))
        self.labelMoveTo.setText(QCoreApplication.translate("FiberCharacterization",u"Move By (um)",None))
        self.labelFiberNumber.setText(QCoreApplication.translate("FiberCharacterization", u"Fiber Number", None))
        self.folderName.setText(QCoreApplication.translate("FiberCharacterization", u"FiberAblation", None))
        self.background.setText(QCoreApplication.translate("FiberCharacterization", u"Background? (T/F)", None))
        self.labelFolderName.setText(QCoreApplication.translate("FiberCharacterization", u"Folder Name", None))
    def connect_to_camera(self, serial):
        camera = None
        for x in range(len(self.instrumentList)):
                # this is the serial number for the camera and needs to be changed if camera is switched
                if self.instrumentList[x]['serial'] == serial:
                    camera = instrument(self.instrumentList[x])
                    break
        #camera.start_live_video()
        return camera

    def change_filepath(self):
        self.filepath = self.parentPath+'/'+self.users.currentItem().text()+'/'+self.folderName.toPlainText()+'/'+self.today
    
    def start_video(self):
        self.timer.start(self.timeBetweenFrames)
        self.camera.start_live_video(exposure_time=self.exposureTime.value())
        self.live = True
        self.timer.timeout.connect(self.view_camera)

    def change_exposure(self):
        if self.live:
            self.camera.stop_live_video()
            self.camera.start_live_video(exposure_time=self.exposureTime.value())
            
    def view_camera(self):
        self.cameraImage.setImage(self.camera.latest_frame())
        
    def grab_image(self):
        self.image = self.camera.latest_frame()
        self.image = self.image.astype(np.uint8)
        return self.image
        
    def save_image(self, data, filename):
        if not os.path.isdir(self.filepath):
            os.makedirs(self.filepath)
        plt.imsave(self.filepath+"/"+filename+".tiff",self.image)
        time.sleep(0.1)
        
    def change_exposure(self,time):
        self.camera._set_exposure(time)

    def capture_image(self):
        if self.background.isChecked():
            self.save_image(self.grab_image(),f"fiber{self.fiberNumber.value()}_interference_bg")
        elif self.live:
            for i in range(5): # we use 5 images for our averaging
                image_array = np.zeros(shape=(1024,1280,int(self.averageNumber.value())))
                for j in range(int(self.averageNumber.value())):
                    image_array[:,:,j] = self.grab_image()
                    time.sleep(self.delayTime.value()//1000)
                for j in range(int(self.averageNumber.value())):
                    self.save_image(image_array[:,:,j],f"fiber{self.fiberNumber.value()}_interference_{i}_{j}")
                self.ecc.move_to(self.axis,int(self.stepSize.value()))
        else:
            print("Must have turned the live video on before trying to capture images")

    def move_attocube(self):
        value = int(self.moveBy.value()*1000)
        self.ecc.move_to(self.axis,target=value)
    # retranslateUi
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    FiberCharacterization = QMainWindow()
    ui = Ui_FiberCharacterization()
    ui.setupUi(FiberCharacterization)
    FiberCharacterization.show()
    sys.exit(app.exec_())
    ui.ecc.close()
