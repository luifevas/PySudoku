
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import levelwindow
class VentanaNivel(QMainWindow,levelwindow.Ui_LevelWindow):
    def __init__(self,parent=None):
        super(VentanaNivel,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.jugar, SIGNAL("clicked()"),self.closeclicked)
        self.connect(self.back, SIGNAL("clicked()"),self.closeclicked)
                    
    def closeclicked(self):
        self.close() 


  
        