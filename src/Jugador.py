'''
Created on 31/07/2013

@author: Administrador
'''
from PyQt4 import QtCore,QtGui

class Jugador():
    '''
    classdocs
    '''

    nombre=''
    tiempo=0
    dificultad=0
    puntos=0
    
    def __init__(self,nombre,dificultad):
        '''
        Constructor
        '''
        self.nombre=nombre
        self.dificultad=dificultad
    
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
