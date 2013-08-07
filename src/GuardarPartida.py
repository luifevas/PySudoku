from Tablero import Tablero

class GuardarPartida(object):
    
    tablero=""

    def __init__(self,tabla):
        '''
        Constructor
        '''
        self.board=tabla
    
    def guardarJugador(self):
        
        fout = open("guardarPartida", "w")
        listacasilla=self.board.getAllCasillas
        
        for elemento in listacasilla:
            if elemento.isLocked()():
                fout.write(str(elemento.getValue()())+","+str(1)+",")
            else:
                fout.write(str(elemento.getValue())+","+str(0)+",")
            
            
        fout.close()