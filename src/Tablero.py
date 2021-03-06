'''
Created on 31/07/2013

@author: Administrador
'''


from Casilla import Casilla
from Jugador import Jugador
import random
from PyQt4 import QtGui,QtCore, QtGui
from sudokuwindow import Ui_SudokuWindow
from ventanaSud import VentanaSud
from lib import UICasilla
from lib import libSudoku
from LCDNumber import LCDNumber
class Tablero:
    '''
    classdocs
    '''
    casillas=[]
    casillasSudoku=[] #casillas listo para jugar

    casillasJuego=[]
    listaQLineEdit=[]
    jugador=''
    MainWindow=''
    reloj=''
    x=''
    def __init__(self,nombre,numPista):
        '''
        Constructor
        '''        
        self.jugador=Jugador(nombre,numPista)
        for i in range(1,10):
            for j in range(1,10):
                k=0
                k=self.buscarRegion(i,j)
                a=Casilla(i,j,k)
                self.casillas.append(a)
        self.copiarTabla(self.casillas, self.casillasSudoku)
        self.colocarPista(numPista)
        self.copiarTabla(self.casillasSudoku, self.casillasJuego)
        self.MainWindow = VentanaSud()
        self.reloj= LCDNumber()
        self.MainWindow.relojLayout.addWidget(self.reloj)
        #for i in range(0,9):
            #for j in range(0,9):
                #x=QtGui.QLineEdit()
                #self.MainWindow.connect(x, QtCore.SIGNAL("editingFinished()"),self.checkSudoku)
                #self.listaQLineEdit.append(x)
                #self.MainWindow.sudokuLayout.addWidget(x,i,j)
        self.x=UICasilla.Board()
        self.llenarSudoku(self.x)
        self.MainWindow.tableroLayout.addWidget(self.x)
        self.llenarUI()
        #self.MainWindow.connect(self.MainWindow.pushButton,QtCore.SIGNAL("clicked()"),self.guardarPartida())
        for casilla in self.x.getAllCasillas():
            self.MainWindow.connect(casilla,QtCore.SIGNAL("valueChanged()"),self.checkSudoku)
        self.MainWindow.show()
    
    
    def checkSudoku(self):
        listaCasillas=self.x.getAllCasillas()
        listaCasillasValues = [c.value for c in listaCasillas]
        listaListaCasillasValues = [listaCasillasValues[x:x+9] for x in range(0, len(listaCasillasValues), 9)]
        if libSudoku.is_board_valid(listaListaCasillasValues):
            if len([elem for elem in listaCasillasValues if elem < 1 ]) == 0:
                msg=QtGui.QMessageBox()
                msg.setText("Ha completado un Sudoku!.")
                tiempo= ((self.reloj.time.minute())*60)+(self.reloj.time.second())
                self.guardarRanking(self.jugador.getNombre(),tiempo)
                msg.exec_()
                self.MainWindow.close()
                
            
            
            
     
     
    def llenarSudoku(self,b):
        casillas = libSudoku.get_new_board("Easy")
        casillasCompletas = casillas[0]
        casillasAgujeros = casillas[1]
        for i in range(0,9):
            for j in range(0,9):
                cID = i * 9 + j
                v = casillasAgujeros[i][j]
                b.setValue(cID,v)
                b.setMark(cID,False)
                if v < 1:
                    b.setLock(cID,False)
                else:
                    b.setLock(cID, True)
            
            
    def llenarUI(self):
        n=0
        for elemento in self.listaQLineEdit:
            numero=self.casillasSudoku[n].getContenido()
            if numero!=0:
                elemento.setText(str(numero))
                elemento.setEnabled(False) 
            n=n+1
    
    def ObtenerDatosUi(self):
        n=0
        for elemento in self.listaQLineEdit:
            x=elemento.text()
            if(x==''):
                self.casillasJuego[n].setContenido(0)
            else:
                self.casillasJuego[n].setContenido(int(x))
                
            n=n+1
    
    def buscarRegion(self,i,j):

        if ((i>=1 and i<=3) and (j>=1 and j<=3)):
            return 1
        if ((i>=1 and i<=3) and (j>=4 and j<=6)):
            return 2
        if ((i>=1 and i<=3) and (j>=7 and j<=9)):
            return 3
        if ((i>=4 and i<=6) and (j>=1 and j<=3)):
            return 4
        if ((i>=4 and i<=6) and (j>=4 and j<=6)):
            return 5
        if ((i>=4 and i<=6) and (j>=7 and j<=9)):
            return 6
        if ((i>=7 and i<=9) and (j>=1 and j<=3)):
            return 7
        if ((i>=7 and i<=9) and (j>=4 and j<=6)):
            return 8
        if ((i>=7 and i<=9) and (j>=7 and j<=9)):
            return 9
    def verificarHorizontal(self,casilla,casillas):
        x=casilla.getFila()
        y=casilla.getColumna()
        for elemento in casillas:                    
            if(x==elemento.getFila() and y!=elemento.getColumna()):
                if(casilla.getContenido()==elemento.getContenido()):
                    return False                                                
        return True
    
    def verificarVertical(self,casilla,casillas):
        x=casilla.getFila()
        y=casilla.getColumna()
        for elemento in casillas:
            if(x!=elemento.getFila() and y==elemento.getColumna()):
                if(casilla.getContenido()==elemento.getContenido()):
                    return False                                                
        return True
    
    def verificarRecuadro(self,casilla,casillas):
        x=casilla.getFila()
        y=casilla.getColumna()
        region=casilla.getRegion()
        for elemento in casillas:
            if(region==elemento.getRegion() and x!=elemento.getFila() and y!=elemento.getColumna()):
                if(casilla.getContenido()==elemento.getContenido()):
                    return False
        return True
    
    def tableroLleno(self):
        for elemento in self.casillasJuego:
            if(elemento.getContenido()==0):
                return False
        return True
    
    def copiarTabla(self,casillas,casillas2):
       
        for elemento1 in casillas:
            a=Casilla(elemento1.getFila(), elemento1.getColumna(), elemento1.getRegion())
            a.setContenido(elemento1.getContenido())
            a.setHabilitado(elemento1.getHabilitado())
            casillas2.append(a)
            
    
    def colocarPista(self,numPistas):
        cont=0
        rand=0
        random.seed(None)
        for i in range(1,10):
            while (cont<=numPistas):
                for elemento in self.casillasSudoku:
                    if(cont <= numPistas):
                        if(elemento.getRegion()==i):
                            #numero aleatorio entre 0 y 1
                            rand=random.randint(0,1)
                            if(rand==1):
                                elemento.setContenido(0)
                                elemento.setHabilitado(True)
                                cont=cont+1                            
            cont=0        
    
    def esPosible(self,posibilidad,casilla,casillas):
        bandera=True
        if (casilla.getContenido()!=0):
            return False
        casilla.setContenido(posibilidad)
        bandera=self.verificarHorizontal(casilla,casillas)
        if(bandera==False):
            casilla.setContenido(0)
            return False
        
        bandera=self.verificarVertical(casilla,casillas)
        if(bandera==False):
            casilla.setContenido(0)
            return False
    
        bandera=self.verificarRecuadro(casilla.casillas)
        if(bandera==False):
            casilla.setContenido(0)
            return False
        casilla.setContenido(0)
        return True
    
        
    def listaDePosibilidades(self,casilla,casillas):        
        posibilidad=[]
        for i in range(1,10):
            if(self.esPosible(i,casilla,casillas)):
                posibilidad.append(i);
        return posibilidad;
    
    def jugadasIncorrectas(self):
        for elemento in self.casillasJuego:
            if(elemento.getContenido()<10 and elemento.getContenido()>0):
                if(not(self.verificarHorizontal(elemento,self.casillasJuego)) and not(self.verificarVertical(elemento,self.casillasJuego)) and not(self.verificarRecuadro(elemento,self.casillasJuego))):
                    #cambio de color de casilla o advertencia de un numero mal ingresado
                    return False
            else:
                #cambio de color de casilla o advertencia de un numero mal ingresado   
                return False
        
        
    def jugadasInvalidas(self):
        k=0
        for elemento in self.casillasJuego:
            if(elemento.getContenido()<10 and elemento.getContenido()>0):
                if(elemento.getContenido()!=self.casillas[k].getContenido()):
                    #advertencia de un numero mal ingresado
                    return False
            else:
                #advertencia de un numero mal ingresado
                return False
            k=k+1
    def guardarRanking(self,nombre,tiempo):
        fout=open("ranking.txt","w")
        fout.write(nombre+","+str(tiempo))
        
    def guardarPartida(self):
        self.Guardar()
    
    def Guardar(self):
        fout = open("guardarPartida.txt", "w")
        listacasilla=self.x.getAllCasillas()
        
        for elemento in listacasilla:
            if elemento.isLocked()():
                fout.write(str(elemento.getValue()())+","+str(1)+",")
            else:
                fout.write(str(elemento.getValue())+","+str(0)+",")
            
            
        fout.close() 
        