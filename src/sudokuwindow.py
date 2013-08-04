# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudokuwindow.ui'
#
# Created: Sat Aug  3 08:42:19 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from LCDNumber import LCDNumber

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(782, 576)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 30, 481, 351))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.sudokuLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.sudokuLayout.setMargin(0)
        self.sudokuLayout.setObjectName(_fromUtf8("sudokuLayout"))
        self.Validar = QtGui.QPushButton(self.centralwidget)
        self.Validar.setGeometry(QtCore.QRect(640, 60, 75, 23))
        self.Validar.setObjectName(_fromUtf8("Validar"))
        self.Cargar = QtGui.QPushButton(self.centralwidget)
        self.Cargar.setGeometry(QtCore.QRect(640, 110, 75, 23))
        self.Cargar.setObjectName(_fromUtf8("Cargar"))
        self.Guardar = QtGui.QPushButton(self.centralwidget)
        self.Guardar.setGeometry(QtCore.QRect(640, 160, 75, 23))
        self.Guardar.setObjectName(_fromUtf8("Guardar"))
        self.pista = QtGui.QPushButton(self.centralwidget)
        self.pista.setGeometry(QtCore.QRect(640, 210, 75, 23))
        self.pista.setObjectName(_fromUtf8("pista"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(620, 290, 121, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 410, 451, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.relojLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.relojLayout.setMargin(0)
        self.relojLayout.setObjectName(_fromUtf8("relojLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.relojLayout.addWidget(LCDNumber())
            

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Validar.setText(_translate("MainWindow", "Validar", None))
        self.Cargar.setText(_translate("MainWindow", "Cargar", None))
        self.Guardar.setText(_translate("MainWindow", "Guardar", None))
        self.pista.setText(_translate("MainWindow", "Pista", None))
        self.checkBox.setText(_translate("MainWindow", "Jugadas Invalidas", None))



