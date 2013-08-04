'''
Created on 04/08/2013

@author: Administrador
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sudokuwindow

class VentanaSud(QMainWindow,sudokuwindow.Ui_SudokuWindow):
    '''
    classdocs
    '''
    
    def __init__(self,parent=None):
        '''
        Constructor
        '''
        super(VentanaSud,self).__init__(parent)        
        self.setupUi(self)
        #self.connect(self.jugar, SIGNAL("clicked()"),self.abrirLevel)
