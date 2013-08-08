from PyQt4 import QtCore,QtGui

class CargarPartida(object):
    lista=''
    tablero=''

    def __init__(self,board):
        '''
        Constructor
        '''

    def cargarJugador(self):
        
        
        fout = open("guardarPartida", "r")
        
        lines=fout.readlines()
        
        listaNumeros=lines[0].split(",")
        listaNumeros.pop()
        self.lista= listaNumeros
        i=0
        k=0
        
        for i in range(0,81):
            self.tablero.setValue(i,self.lista[k])
            if int(listaNumeros[i+1])==1:
                self.tablero.setLock(i,True)
            else:
               self.tablero.setLock(i,False)
            i=i+2    
        
        
        
            
            
        fout.close()