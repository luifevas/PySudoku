#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

""" Smallest widget that resembles one sudoku field

    This is the smallest widget. It allows for setting one value
    and 4 auxiliary values.
"""
class CasillaWidget(QtGui.QWidget):
    
    def __init__(self, value, cId, locked = False, wheelEnabled = True ):
        super(CasillaWidget, self).__init__()
        self.marked = False
        self.locked = locked
        self.value = value
        self.initUI()
        self.auxValue = [0, 0, 0, 0]
        self.wheelEnabled = wheelEnabled
        
    def setLock(self, lock):
        self.locked = lock
        
    def setMark(self, mark):
        self.marked = mark
        self.repaint()

    def setValue(self, v):
        self.value = v
        self.repaint()
        
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
        if self.marked:
            rectBg = QtGui.QColor(255, 180, 180) if self.locked else QtGui.QColor(255, 240, 240)
        else:
            rectBg = QtGui.QColor(180, 180, 180) if self.locked else QtGui.QColor(240, 240, 240)
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

""" Group of 9 Casillas    
    
    A Container Widget that stores 9 Casillas
"""
class Group(QtGui.QWidget):
    
    def __init__(self, gId):
        super(Group, self).__init__()
        self.gId = gId
        self.casillas = []

        self.initUI()
        
    def getCasilla(self, xs):
        return self.casillas[xs]
        
    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid) 
        for i in range(0, 3):
            for j in range(0, 3):
                locked = False;
                if i % 2 == 0: 
                    locked = True;
                cId = self.gId * 27 + i * 9 + j
                cas = CasillaWidget(i + j, cId,locked)
                self.casillas.append(cas)
                grid.addWidget(cas, i, j)
        self.setWindowTitle('CasillaWidget Example')
        #self.show()

""" A Sudoku board, consisting of 9 Groups of Casillas 
        
    All Casillas of the Board have an cId starting from 
    0 through 80. The cId are distributed by row. That means:
    The top left casilla has the cId 0. The
    3rd Casilla in the first row has the cId 3. The first 
    Casilla of the third row has the cId 18 and so on.
"""  
class Board(QtGui.QWidget):
    
    """ returns a List of all casillas (cId 0 through cId 80)"""
    def getAllCasillas(self):
        toReturn = []
        for i in range(0, 81):
            toReturn.append(self.getCasilla(i))
        return toReturn
    
    def setValue(self, cId , v):
        self.getCasilla(cId).setValue(v)

    def setMark(self, cId, mark):
        self.getCasilla(cId).setMark(mark)

    def lockField(self, cId):
        self.getCasilla(cId).setLock(True)
    
    def getCasilla(self, cId):
        (gId, xs) = _cIdToGroup(cId);
        print(gId)
        print(xs)
        return self.groups[gId].getCasilla(xs)

    def __init__(self):
        super(Board, self).__init__()
        self.groups = []
        self.initUI()
        
    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        for i in range(0,3):
            for j in range(0,3):
                gId = i * 3 + j
                g = Group(gId)
                self.groups.append(g)
                grid.addWidget(g, i, j)
        self.setMark(0, True)
        self.setMark(80, True)
        self.setMark(56, True)
        self.setWindowTitle('Sudoku Field')
        self.show()
        
#Helpers 
        
def _cIdToGroup(cId):
    groupCol = cId // 3 % 3
    groupRow = cId // 27
    row = cId // 9
    col = cId % 9 
    rowXs = row - groupRow * 3
    colXs = col - groupCol * 3
    xs = rowXs * 3 + colXs 
    gId = groupRow * 3 + groupCol
    return (gId, xs)

# main
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    b = Board()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
