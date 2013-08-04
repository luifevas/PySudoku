#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class CasillaWidget(QtGui.QWidget):
    
    def __init__(self, value = -1, locked = True ):
        super(CasillaWidget, self).__init__()
        self.locked = locked
        self.value = value
        self.initUI()
        self.auxValue = [0, 0, 0, 0]
        
    def mousePressEvent(self, event):
        if not self.locked:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.value = (self.value + 1) % 10 
            else:
                pos = event.pos()
                i = 0;
                print(pos)
                print(pos.x())
                print(pos.y())
                if ( pos.x() > 35 ):
                    if ( pos.y() > 35): i = 3
                    else: i = 1
                else:
                    if ( pos.y() > 35): i = 2
                    else: i = 0
                print(i)
                self.auxValue[i] = (self.auxValue[i] + 1) % 10;
        self.repaint()
        
        
    def initUI(self):
        self.setMinimumSize(1, 30)
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
        
    def drawWidget(self, qp):
        #draw border
        rectBg = QtGui.QColor(200, 200, 200) if self.locked else QtGui.QColor(240, 240, 240)
        qp.setPen(QtGui.QColor(255, 255, 255))
        qp.fillRect(0,0, 70, 70, rectBg)

        #draw main value
        if self.value > 0:
            font = QtGui.QFont('Serif', 15, QtGui.QFont.Light)
            qp.setFont(font)
            fontColor = QtGui.QColor(50,50,50) if self.locked else QtGui.QColor(0,0,255)
            qp.setPen(fontColor)
            qp.drawText(30, 41 ,str(self.value))

        #draw aux values
        auxPos = ((5,15),(57,15),(5,65), (57,65))
        font = QtGui.QFont('Serif', 8, QtGui.QFont.Light)
        fontColor = QtGui.QColor(50,50,50);
        qp.setFont(font)
        qp.setPen(fontColor)
        for i,aux in enumerate(self.auxValue):
            #TODO change
            if aux > 0:
                qp.drawText(auxPos[i][0],auxPos[i][1], str(aux))
                    

        
class Group(QtGui.QWidget):
    
    def __init__(self):
        super(Group, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid) 
        for i in range(0, 3):
            for j in range(0, 3):
                locked = False;
                if i % 2 == 0: 
                    locked = True;
                cas = CasillaWidget(i + j, locked)
                grid.addWidget(cas, i, j)
        self.setWindowTitle('CasillaWidget Example')
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    gr = Group()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
         
        
        
        
        
        
    
        
    
    