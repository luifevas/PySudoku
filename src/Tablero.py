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
class Tablero:
    '''
    classdocs
    '''

    casillas=[]
    casillasSudoku=[]
    casillasJuego=[]
    listaQLineEdit=[]
    jugador=''
    MainWindow=''
    
    def __init__(self,nombre,numPista):
        '''
        Constructor
        '''        
        self.jugador=Jugador(nombre,numPista)
        for i in range(1,10):
            for j in range(1,10):
                k=self.buscarRegion(i,j)
                a=Casilla(i,j,k)
                self.casillas.append(a)
        self.copiarTabla(self.casillas, self.casillasSudoku)
        self.colocarPista(numPista)
        self.copiarTabla(self.casillasSudoku, self.casillasJuego)
        self.MainWindow = VentanaSud()
        #for i in range(0,9):
            #for j in range(0,9):
                #x=QtGui.QLineEdit()
                #self.MainWindow.connect(x, QtCore.SIGNAL("editingFinished()"),self.checkSudoku)
                #self.listaQLineEdit.append(x)
                #self.MainWindow.sudokuLayout.addWidget(x,i,j)
        x=UICasilla.Board()
        self.MainWindow.tableroLayout.addWidget(x)
        self.llenarUI()
        self.MainWindow.show()
    
    
    def checkSudoku(self):
        bandera=1
        self.ObtenerDatosUi()
        if(self.tableroLleno()):
            bandera=1
            for i in range(0,81):
                if(self.casillasJuego[i].getContenido()>0 and self.casillasJuego[i].getContenido()<10):
                    if(not(self.verificarRecuadro(self.casillasJuego[i],self.casillasJuego) and self.verificarHorizontal(self.casillasJuego[i],self.casillasJuego) and self.verificarVertical(self.casillasJuego[i],self.casillasJuego))):
                        #mensaje de Finalizacion del juego
                        bandera=0
                        #QtGui.QMessageBox.information(self.MainWindow,"Mensaje","Sudoku Mal Resuelto")
                        print("Sudoku Mal Resuelto")
                        break
                else:
                    bandera=0
            if (bandera==1):
                self.MainWindow.close()
                QtGui.QMessageBox.information(self.MainWindow,"Mensaje","Sudoku Resuelto")
                print("Sudoku Resuelto")
        else:
            print("Sudoku Incompleto")
        
    def llenarUI(self):
        for n, elemento in enumerate(self.listaQLineEdit):
            numero=self.casillasSudoku[n].getContenido()
            if numero!=0:
                elemento.setText(str(numero))
                elemento.setEnabled(False) 
    
    def ObtenerDatosUi(self):
        for n, elemento in enumerate(self.listaQLineEdit):
            x=elemento.text()
            if(x==''):
                self.casillasJuego[n].setContenido(0)
            else:
                self.casillasJuego[n].setContenido(int(x))
    
    def buscarRegion(self,i,j):
        return ((i - 1)// 3 * 3) + (j - 1)// 3 + 1
        
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
        for k,elemento in enumerate(self.casillasJuego):
            if(elemento.getContenido()<10 and elemento.getContenido()>0):
                if(elemento.getContenido()!=self.casillas[k].getContenido()):
                    #advertencia de un numero mal ingresado
                    return False
            else:
                #advertencia de un numero mal ingresado
                return False
    
        