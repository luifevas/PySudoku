'''
Created on 31/07/2013

@author: Administrador
'''


from Casilla import Casilla
import random
from PyQt4 import QtCore,QtGui
from sudokuwindow import Ui_SudokuWindow

class Tablero:
    '''
    classdocs
    '''

    casillas=[]
    casillasSudoku=[]
    listaQLineEdit=[]
    MainWindow=''
    
    def __init__(self,numPista):
        '''
        Constructor
        '''        
        for i in range(1,10):
            for j in range(1,10):
                k=0
                k=self.buscarRegion(i,j)
                a=Casilla(i,j,k)
                self.casillas.append(a)
        self.copiarTabla(self.casillas, self.casillasSudoku)
        self.colocarPista(numPista)
        self.MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.MainWindow)
        for i in range(0,9):
            for j in range(0,9):
                x=QtGui.QLineEdit()
                self.listaQLineEdit.append(x)
                ui.sudokuLayout.addWidget(x,i,j)
        self.llenarUI()
        self.MainWindow.show()
        
    def llenarUI(self):
        n=0
        for elemento in self.listaQLineEdit:
            numero=self.casillasSudoku[n].getContenido()
            if numero!=0:
                elemento.setText(str(numero))
                elemento.setEnabled(False) 
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
        
    def verificarHorizontal(self,casilla):
        x=casilla.getFila()
        y=casilla.getColumna()
        for elemento in self.casillasSudoku:                    
            if(x==elemento.getFila() and y!=elemento.getColumna()):
                if(casilla.getContenido()==elemento.getContenido()):
                    return False                                                
        return True
    
    def verificarVertical(self,casilla):
        x=casilla.getFila()
        y=casilla.getColumna()
        for elemento in self.casillasSudoku:
            if(x!=elemento.getFila() and y==elemento.getColumna()):
                if(casilla.getContenido()==elemento.getContenido()):
                    return False                                                
        return True
    
    def verificarRecuadro(self,casilla):
        x=casilla.getFila()
        y=casilla.getColumna()
        region=casilla.getRegion()
        for elemento in self.casillasSudoku:
            if(region==elemento.getRegion() and x!=elemento.getFila() and y!=elemento.getColumna()):
                if(casilla.getContenido()==elemento.getContenido()):
                    return False
        return True
    
    def tableroLleno(self):
        for elemento in self.casillasSudoku:
            if(elemento.getContenido()==0):
                return False
        return True
    
    def copiarTabla(self,casillas,casillas2):
       
        for elemento1 in casillas:
            a=Casilla(elemento1.getFila(), elemento1.getColumna(), elemento1.getRegion())
            a.setContenido(elemento1.getContenido())
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
    
    def esPosible(self,posibilidad,casilla):
        bandera=True
        if (casilla.getContenido()!=0):
            return 
        casilla.setContenido(posibilidad)
        bandera=self.verificarHorizontal(casilla)
        if(bandera==False):
            casilla.setContenido(0)
            return False
        
        bandera=self.verificarVertical(casilla)
        if(bandera==False):
            casilla.setContenido(0)
            return False
    
        bandera=self.verificarRecuadro(casilla)
        if(bandera==False):
            casilla.setContenido(0)
            return False
        casilla.setContenido(0)
        return True
    
        
    def listaDePosibilidades(self,casilla):        
        posibilidad=[]
        for i in range(1,10):
            if(self.esPosible(i,casilla)):
                posibilidad.append(i);
        return posibilidad;
    
    def jugadasIncorrectas(self):
        for elemento in self.casillasSudoku:
            if(elemento.getContenido()<10 and elemento.getContenido()>0):
                if not(self.verificarHorizontal(elemento)):
                    print("error en horizontal")
                if not(self.verificarVertical(elemento)):
                    print("error en vertical")
                if not(self.verificarRecuadro(elemento)):
                    print("error en recuadro")
                if(not(self.verificarHorizontal(elemento)) and not(self.verificarVertical(elemento)) and not(self.verificarRecuadro(elemento))):
                    #cambio de color de casilla o advertencia de un numero mal ingresado
                    print("1 "+str(elemento.getFila())+" "+str(elemento.getColumna()))
                    return False
            else:
                #cambio de color de casilla o advertencia de un numero mal ingresado   
                print("2 "+str(elemento.getFila())+" "+str(elemento.getColumna()))
                return False
        
        
    def jugadasInvalidas(self):
        k=0
        for elemento in self.casillasSudoku:
            if(elemento.getContenido()<10 and elemento.getContenido()>0):
                if(elemento.getContenido()!=self.casillas[k].getContenido()):
                    #advertencia de un numero mal ingresado
                    print(str(elemento.getFila())+" "+str(elemento.getColumna()))
                    return False
            else:
                #advertencia de un numero mal ingresado
                print(str(elemento.getFila())+" "+str(elemento.getColumna()))
                return False
            k=k+1
    
        