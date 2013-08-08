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
        fout = open("ranking.txt", "r")
        lines= fout.readlines()
        listanombres=lines[0].split(",")
        for i in range(0,len(listanombres)):
            index1 = model.index(i,0,QModelIndex())
            model.setData(index1,listanombres[i])
            index2 = model.index(i,1,QModelIndex())
            model.setData(index2,listanombres[i])

        
        
    def backclicked(self):
        self.close();
        
        
        
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana=VentanaRanking()
    ventana.show()
    app.exec_()
    pass
    