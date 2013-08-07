'''
Created on 07/08/2013

@author: LuisFer
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import rankingwindow
class VentanaRanking(QMainWindow,rankingwindow.Ui_RankingWindow):
    Jugadores=[]
    def __init__(self,parent=None):
        super(VentanaRanking,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.back, SIGNAL("clicked()"),self.backclicked)
        #self.Jugadores=cargarJugadores
        model=QStandardItemModel(20,2,self)
        model.setHorizontalHeaderItem(0,QStandardItem("Nombre"))
        model.setHorizontalHeaderItem(1,QStandardItem("Puntaje"))
        self.tableView.setModel(model)
        
    def backclicked(self):
        self.close();
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana=VentanaRanking()
    ventana.show()
    app.exec_()
    pass
    