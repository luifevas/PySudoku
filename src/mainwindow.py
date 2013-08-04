# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Aug  3 12:42:12 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from levelwindow import Ui_LevelWindow
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
    a=''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(761, 515)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 131, 121))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../Desktop/logosudoku.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.jugar = QtGui.QPushButton(self.centralwidget)
        self.jugar.setGeometry(QtCore.QRect(320, 180, 75, 23))
        self.jugar.setObjectName(_fromUtf8("jugar"))
        MainWindow.connect(self.jugar, QtCore.SIGNAL("clicked()"),self.abrirLevel)
        self.cargar = QtGui.QPushButton(self.centralwidget)
        self.cargar.setGeometry(QtCore.QRect(320, 220, 75, 23))
        self.cargar.setObjectName(_fromUtf8("cargar"))
        self.salir = QtGui.QPushButton(self.centralwidget)
        self.salir.setGeometry(QtCore.QRect(320, 290, 75, 23))
        self.salir.setObjectName(_fromUtf8("salir"))
        self.acerca = QtGui.QPushButton(self.centralwidget)
        self.acerca.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.acerca.setObjectName(_fromUtf8("acerca"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.jugar.setText(_translate("MainWindow", "Jugar", None))
        self.cargar.setText(_translate("MainWindow", "Cargar", None))
        self.salir.setText(_translate("MainWindow", "Salir", None))
        self.acerca.setText(_translate("MainWindow", "Acerca de..", None))
    
    def abrirLevel(self):
        self.a=QtGui.QMainWindow()
        ui=Ui_LevelWindow()
        ui.setupUi(self.a)
        self.a.show()
        #instanciar la clase
        print("hola")

