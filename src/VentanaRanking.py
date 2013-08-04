'''
Created on 03/08/2013

@author: LuisFer
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import rankingwindow
from main import VentanaPrincipal
class VentanaRanking(QMainWindow,rankingwindow.Ui_MainWindow):
    


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(VentanaRanking,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.back,SIGNAL("clicked()"),self.backclicked)
        
        
        
    def backclicked(self):
        vp= VentanaPrincipal()
        self.close()
        vp.show()
        
    if __name__ == '__main__':
        import sys
        from VentanaRanking import VentanaRanking
        app = QApplication(sys.argv)
        ventana=VentanaRanking()
        ventana.show()
        app.exec_()
        pass