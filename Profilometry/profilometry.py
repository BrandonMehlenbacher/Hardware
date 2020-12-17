# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profilometryJRAlnk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_profilometry(object):
    def setupUi(self, profilometry):
        if not profilometry.objectName():
            profilometry.setObjectName(u"profilometry")
        profilometry.resize(1079, 329)
        self.centralwidget = QWidget(profilometry)
        self.centralwidget.setObjectName(u"centralwidget")
        self.initCamera = QPushButton(self.centralwidget)
        self.initCamera.setObjectName(u"initCamera")
        self.initCamera.setGeometry(QRect(70, 80, 131, 41))
        self.live = QPushButton(self.centralwidget)
        self.live.setObjectName(u"live")
        self.live.setGeometry(QRect(230, 80, 131, 41))
        self.capture = QPushButton(self.centralwidget)
        self.capture.setObjectName(u"capture")
        self.capture.setGeometry(QRect(390, 80, 131, 41))
        self.stopLive = QPushButton(self.centralwidget)
        self.stopLive.setObjectName(u"stopLive")
        self.stopLive.setGeometry(QRect(550, 80, 131, 41))
        self.loadParameter = QPushButton(self.centralwidget)
        self.loadParameter.setObjectName(u"loadParameter")
        self.loadParameter.setGeometry(QRect(710, 80, 131, 41))
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(870, 80, 131, 41))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 180, 191, 31))
        self.file = QLabel(self.centralwidget)
        self.file.setObjectName(u"file")
        self.file.setGeometry(QRect(70, 160, 55, 16))
        self.stepSize = QSpinBox(self.centralwidget)
        self.stepSize.setObjectName(u"stepSize")
        self.stepSize.setGeometry(QRect(310, 180, 101, 31))
        self.stepSize.setMaximum(1000)
        self.stepSize.setValue(128)
        self.labelStepSize = QLabel(self.centralwidget)
        self.labelStepSize.setObjectName(u"labelStepSize")
        self.labelStepSize.setGeometry(QRect(310, 160, 101, 16))
        self.labelStepSize_2 = QLabel(self.centralwidget)
        self.labelStepSize_2.setObjectName(u"labelStepSize_2")
        self.labelStepSize_2.setGeometry(QRect(470, 160, 121, 16))
        self.stepSize_2 = QSpinBox(self.centralwidget)
        self.stepSize_2.setObjectName(u"stepSize_2")
        self.stepSize_2.setGeometry(QRect(470, 180, 101, 31))
        self.stepSize_2.setLayoutDirection(Qt.LeftToRight)
        self.stepSize_2.setFrame(True)
        self.stepSize_2.setReadOnly(False)
        self.stepSize_2.setMaximum(100)
        self.stepSize_2.setValue(17)
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(640, 180, 221, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(640, 160, 121, 16))
        profilometry.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(profilometry)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1079, 26))
        profilometry.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(profilometry)
        self.statusbar.setObjectName(u"statusbar")
        profilometry.setStatusBar(self.statusbar)

        self.retranslateUi(profilometry)

        self.listWidget.setCurrentRow(0)


        QMetaObject.connectSlotsByName(profilometry)
    # setupUi

    def retranslateUi(self, profilometry):
        profilometry.setWindowTitle(QCoreApplication.translate("profilometry", u"MainWindow", None))
        self.initCamera.setText(QCoreApplication.translate("profilometry", u"Init Camera", None))
        self.live.setText(QCoreApplication.translate("profilometry", u"Live", None))
        self.capture.setText(QCoreApplication.translate("profilometry", u"Capture", None))
        self.stopLive.setText(QCoreApplication.translate("profilometry", u"Stop Live", None))
        self.loadParameter.setText(QCoreApplication.translate("profilometry", u"Load Parameter", None))
        self.stop.setText(QCoreApplication.translate("profilometry", u"Stop", None))
        self.textEdit.setHtml(QCoreApplication.translate("profilometry", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fiber1_</p></body></html>", None))
        self.file.setText(QCoreApplication.translate("profilometry", u"File", None))
        self.labelStepSize.setText(QCoreApplication.translate("profilometry", u"Step Size (nm)", None))
        self.labelStepSize_2.setText(QCoreApplication.translate("profilometry", u"milliseconds to wait", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("profilometry", u"Brandon Mehlenbacher", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("profilometry", u"Beau", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("profilometry", u"Lisa-Maria", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("profilometry", u"Julia", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("profilometry", u"Alex Fairhall", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("profilometry", u"Name of User", None))
    # retranslateUi

