# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudokuwindow.ui'
#
# Created: Tue Aug  6 22:42:25 2013
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

class Ui_SudokuWindow(object):
    def setupUi(self, SudokuWindow):
        SudokuWindow.setObjectName(_fromUtf8("SudokuWindow"))
        SudokuWindow.resize(1200, 700)
        self.centralwidget = QtGui.QWidget(SudokuWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.tableroLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.tableroLayout.setMargin(0)
        self.tableroLayout.setObjectName(_fromUtf8("tableroLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 50, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 90, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 140, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1000, 190, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(1000, 310, 81, 31))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(149, 601, 501, 71))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.relojLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.relojLayout.setMargin(0)
        self.relojLayout.setObjectName(_fromUtf8("relojLayout"))
        SudokuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SudokuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SudokuWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SudokuWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SudokuWindow.setStatusBar(self.statusbar)
        self.relojLayout.addWidget(LCDNumber())
        self.retranslateUi(SudokuWindow)
        QtCore.QMetaObject.connectSlotsByName(SudokuWindow)

    def retranslateUi(self, SudokuWindow):
        SudokuWindow.setWindowTitle(_translate("SudokuWindow", "MainWindow", None))
        self.pushButton.setText(_translate("SudokuWindow", "Cargar", None))
        self.pushButton_2.setText(_translate("SudokuWindow", "Guardar", None))
        self.pushButton_3.setText(_translate("SudokuWindow", "Pista!", None))
        self.pushButton_4.setText(_translate("SudokuWindow", "Validar", None))
        self.checkBox.setText(_translate("SudokuWindow", "Validar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SudokuWindow = QtGui.QMainWindow()
    ui = Ui_SudokuWindow()
    ui.setupUi(SudokuWindow)
    SudokuWindow.show()
    sys.exit(app.exec_())

