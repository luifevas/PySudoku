# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'levelwindow.ui'
#
# Created: Sat Aug  3 13:10:13 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(614, 445)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 150, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.level = QtGui.QComboBox(self.centralwidget)
        self.level.setGeometry(QtCore.QRect(170, 150, 69, 22))
        self.level.setObjectName(_fromUtf8("level"))
        self.level.addItem(_fromUtf8(""))
        self.level.addItem(_fromUtf8(""))
        self.level.addItem(_fromUtf8(""))
        self.name = QtGui.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(350, 150, 113, 20))
        self.name.setObjectName(_fromUtf8("name"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(170, 280, 75, 23))
        self.back.setObjectName(_fromUtf8("back"))
        self.jugar = QtGui.QPushButton(self.centralwidget)
        self.jugar.setGeometry(QtCore.QRect(350, 280, 75, 23))
        self.jugar.setObjectName(_fromUtf8("jugar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Dificultad:", None))
        self.level.setItemText(0, _translate("MainWindow", "Fácil", None))
        self.level.setItemText(1, _translate("MainWindow", "Medio", None))
        self.level.setItemText(2, _translate("MainWindow", "Difícil", None))
        self.label_2.setText(_translate("MainWindow", "Nombre:", None))
        self.back.setText(_translate("MainWindow", "Atrás", None))
        self.jugar.setText(_translate("MainWindow", "Jugar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

