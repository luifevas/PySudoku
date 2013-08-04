'''
Created on 03/08/2013

@author: Administrador
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mainwindow

class VentanaPrincipal(QMainWindow,mainwindow.Ui_MainWindow):
    def __init__(self,parent=None):
        super(VentanaPrincipal,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.jugar, SIGNAL("clicked()"),self.jugarclicked)
                    
    def jugarclicked(self):
        self.close() 
        
                     
    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show()
    app.exec_()
    pass
