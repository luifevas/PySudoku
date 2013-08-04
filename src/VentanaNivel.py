
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import levelwindow
class VentanaNivel(QMainWindow,levelwindow.Ui_LevelWindow):
    def __init__(self,parent=None):
        super(VentanaNivel,self).__init__(parent)
        self.setupUi(self)
        

  
        