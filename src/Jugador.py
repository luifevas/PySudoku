'''
Created on 31/07/2013

@author: Administrador
'''
from Tablero import Tablero



class Jugador():
    '''
    classdocs
    '''

    nombre=''
    tiempo=0
    dificultad=0
    puntos=0
    tablero=''
    
    def __init__(self,nombre,dificultad):
        '''
        Constructor
        '''
        self.nombre=nombre
        self.dificultad=dificultad
        self.tablero=Tablero(dificultad)
    
    #Getters y Setters de la Clase Jugador
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre
        
    def getTiempo(self):
        return self.tiempo
    
    def setTiempo(self,tiempo):
        self.tiempo=tiempo
        
    def getDificultad(self):
        return self.dificultad
    
    def setDificultad(self,dificultad):
        self.dificultad=dificultad
        
    def getPuntos(self):
        return self.puntos
    
    def setPuntos(self,puntos):
        self.puntos=puntos
    
    def getTablero(self):
        return self.tablero
    
    def setTablero(self,tablero):
        self.tablero=tablero
        
    def evento(self):
        if(self.tablero.tableroLleno()):
            for i in range(0,81):
                if(self.tablero.verificarRecuadro(self.tablero.casillas[i]) and self.tablero.verificarHorizontal(self.tablero.casillas[i]) and self.tablero.verificarVertical(self.tablero.casillas[i])):
                    #mensaje de Finalizacion del juego
                    #return True
                    print("Sudoku Resuelto")
                else:
                    #mensaje de Sudoku mal resuelto
                    print("Sudoku Mal Resuelto")
                    return False
