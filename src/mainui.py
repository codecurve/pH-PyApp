# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created: Mon Sep 09 16:00:24 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 241, 481))
        self.groupBox.setObjectName("groupBox")
        self.co2Sink = QtGui.QSlider(self.groupBox)
        self.co2Sink.setGeometry(QtCore.QRect(110, 30, 20, 221))
        self.co2Sink.setOrientation(QtCore.Qt.Vertical)
        self.co2Sink.setTickPosition(QtGui.QSlider.TicksBelow)
        self.co2Sink.setObjectName("co2Sink")
        self.co2SourceLabel = QtGui.QLabel(self.groupBox)
        self.co2SourceLabel.setGeometry(QtCore.QRect(10, 261, 61, 20))
        self.co2SourceLabel.setObjectName("co2SourceLabel")
        self.protonSource = QtGui.QSlider(self.groupBox)
        self.protonSource.setGeometry(QtCore.QRect(190, 30, 20, 221))
        self.protonSource.setOrientation(QtCore.Qt.Vertical)
        self.protonSource.setTickPosition(QtGui.QSlider.TicksBelow)
        self.protonSource.setObjectName("protonSource")
        self.co2SinkLabel = QtGui.QLabel(self.groupBox)
        self.co2SinkLabel.setGeometry(QtCore.QRect(100, 261, 51, 20))
        self.co2SinkLabel.setObjectName("co2SinkLabel")
        self.co2Source = QtGui.QSlider(self.groupBox)
        self.co2Source.setGeometry(QtCore.QRect(30, 30, 20, 221))
        self.co2Source.setOrientation(QtCore.Qt.Vertical)
        self.co2Source.setTickPosition(QtGui.QSlider.TicksBelow)
        self.co2Source.setObjectName("co2Source")
        self.protonSourceValue = QtGui.QLineEdit(self.groupBox)
        self.protonSourceValue.setEnabled(False)
        self.protonSourceValue.setGeometry(QtCore.QRect(170, 291, 51, 20))
        self.protonSourceValue.setObjectName("protonSourceValue")
        self.co2SinkValue = QtGui.QLineEdit(self.groupBox)
        self.co2SinkValue.setEnabled(False)
        self.co2SinkValue.setGeometry(QtCore.QRect(90, 291, 51, 20))
        self.co2SinkValue.setObjectName("co2SinkValue")
        self.protonSourceLabel = QtGui.QLabel(self.groupBox)
        self.protonSourceLabel.setGeometry(QtCore.QRect(170, 261, 61, 20))
        self.protonSourceLabel.setObjectName("protonSourceLabel")
        self.co2SourceValue = QtGui.QLineEdit(self.groupBox)
        self.co2SourceValue.setEnabled(False)
        self.co2SourceValue.setGeometry(QtCore.QRect(10, 291, 51, 20))
        self.co2SourceValue.setObjectName("co2SourceValue")
        self.protonLevelPurge = QtGui.QPushButton(self.groupBox)
        self.protonLevelPurge.setGeometry(QtCore.QRect(10, 330, 75, 23))
        self.protonLevelPurge.setObjectName("protonLevelPurge")
        self.protonPurgeAmount = QtGui.QLineEdit(self.groupBox)
        self.protonPurgeAmount.setGeometry(QtCore.QRect(90, 330, 113, 20))
        self.protonPurgeAmount.setObjectName("protonPurgeAmount")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 20, 361, 481))
        self.groupBox_2.setObjectName("groupBox_2")
        self.logText = QtGui.QPlainTextEdit(self.groupBox_2)
        self.logText.setEnabled(False)
        self.logText.setGeometry(QtCore.QRect(20, 340, 311, 111))
        self.logText.setObjectName("logText")
        self.resetButton = QtGui.QPushButton(self.groupBox_2)
        self.resetButton.setGeometry(QtCore.QRect(110, 280, 75, 23))
        self.resetButton.setObjectName("resetButton")
        self.simulateButton = QtGui.QPushButton(self.groupBox_2)
        self.simulateButton.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.simulateButton.setObjectName("simulateButton")
        self.plotArea = MatplotlibWidget(self.groupBox_2)
        self.plotArea.setGeometry(QtCore.QRect(20, 30, 291, 231))
        self.plotArea.setObjectName("plotArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.co2Source, QtCore.SIGNAL("valueChanged(int)"), self.co2SourceValue.update)
        QtCore.QObject.connect(self.co2Sink, QtCore.SIGNAL("valueChanged(int)"), self.co2SinkValue.update)
        QtCore.QObject.connect(self.protonSource, QtCore.SIGNAL("valueChanged(int)"), self.protonSourceValue.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Adjustments", None, QtGui.QApplication.UnicodeUTF8))
        self.co2SourceLabel.setText(QtGui.QApplication.translate("MainWindow", "CO2 source", None, QtGui.QApplication.UnicodeUTF8))
        self.co2SinkLabel.setText(QtGui.QApplication.translate("MainWindow", "CO2 sink", None, QtGui.QApplication.UnicodeUTF8))
        self.protonSourceLabel.setText(QtGui.QApplication.translate("MainWindow", "H+ source", None, QtGui.QApplication.UnicodeUTF8))
        self.protonLevelPurge.setText(QtGui.QApplication.translate("MainWindow", "H+ purge", None, QtGui.QApplication.UnicodeUTF8))
        self.protonPurgeAmount.setText(QtGui.QApplication.translate("MainWindow", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateButton.setText(QtGui.QApplication.translate("MainWindow", "Simulate", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget