'''
Created on 31/07/2013

@author: Administrador
'''

class Casilla:
    '''
    classdocs
    '''
    
    contenido=0
    fila=0
    columna=0
    habilitado=False
    region=0    
    
    def __init__(self,fila,columna,region):
        '''
        Constructor
        '''
        self.fila=fila
        self.columna=columna
        self.region=region
    
    def setContenido(self,contenido):
        self.contenido=contenido
    def getContenido(self):
        return self.contenido
    
    def setFila(self,fila):
        self.fila=fila
    def getFila(self):
        return self.fila
    
    def setColumna(self,columna):
        self.columna=columna
    def getColumna(self):
        return self.columna
    
    def setHabilitado(self,habilitado):
        self.habilitado=habilitado
    def getHabilitado(self):
        return self.habilitado
    
    def setRegion(self,region):
        self.region=region
    def getRegion(self):
        return self.region
    
