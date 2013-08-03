'''
Created on 03/08/2013

@author: LuisFer
'''
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui


class LCDNumber(QtGui.QWidget):
    '''
    classdocs
    '''
    timer= ""
    time= ""


    def __init__(self):
        '''
        Constructor
        '''
        super(LCDNumber, self).__init__()
        self.initUI()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1)
        self.time= QtCore.QTime()
        self.showlcd()
        
        
    def initUI(self):
        self.lcd = QtGui.QLCDNumber(self)
        self.setGeometry(30, 30, 800, 600)
        self.setWindowTitle('Time')

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lcd)
        self.setLayout(vbox)

        self.show()
    def showlcd(self):
        self.time.setHMS(0,self.time.addMSecs(+1).minute(),self.time.addMSecs(+1).second(),self.time.addMSecs(+1).msec())
      
        text = self.time.toString('hh:mm:ss')
        self.lcd.display(text)
        
   

      

    if __name__ == '__main__':
        from LCDNumber import LCDNumber
        app = QtGui.QApplication(sys.argv)
        lcd=LCDNumber()
        sys.exit(app.exec_())
