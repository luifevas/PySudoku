#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class CasillaWidget(QtGui.QWidget):
    
    def __init__(self, value = -1, cId, locked = True, wheelEnabled = True ):
        super(CasillaWidget, self).__init__()
        self.locked = locked
        self.value = value
        self.initUI()
        self.auxValue = [0, 0, 0, 0]
        self.wheelEnabled = wheelEnabled

    def setValue(self, v):
        pass
        
    def changeValue(self, v):
        self.value = (self.value + v) % 10 
        #emit valueChanged(id, v)
    
    def changeAuxValue(self, v, i):
        self.auxValue[i] = (self.auxValue[i] + v) % 10 
        
    def keyPressEvent(self, event):
        print("bla")
        print(event.key())
        
    def mousePressEvent(self, event):
        if not self.locked:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.changeValue(1)
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
                self.changeAuxValue(1,i)
        self.repaint()
        
    def wheelEvent(self, event):
        if self.wheelEnabled and not self.locked:
            pos = event.pos();
            i = -1 
            if ( pos.x() < 18 and pos.y() < 18 ): i = 0
            elif ( pos.x() > 52 and pos.y() < 18 ): i = 1
            elif ( pos.x() < 18 and pos.y() > 52 ): i = 2
            elif ( pos.x() > 52 and pos.y() > 52 ): i = 3
        #Aux Area
            if i > -1:
                v = 1 if event.delta() > 0 else -1
                self.changeAuxValue(v,i)
        #Normal Value    
            else:
                v = 1 if event.delta() > 0 else -1
                self.changeValue(v)
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
        #self.show()
        
        
class Field(QtGui.QWidget):
    def setValue(self, cId , v):
        pass

    def markField(self, cId):
        pass

    def lockField(self, cId):
        pass

    def __init__(self):
        super(Field, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        for i in range(0,3):
            for j in range(0,3):
                g = Group()
                grid.addWidget(g, i, j)
        self.setWindowTitle('Sudoku Field')
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    f = Field()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
