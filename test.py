import unittest
from Monopolio import *
#from Celda import Celda
#from Persona import Persona
#from Juego import Juego

class Test(unittest.TestCase):
    def test1(self):
        celda1 = Celda("Janina", 1, "Propiedad", 150, 50)
        persona1 = Persona("Cristina", 140,"si")
        juego = Juego()
        msg = juego.validar_movimiento(celda1,persona1)
        self.assertEquals(msg,"Perdio")

if __name__ == '__main__':
    unittest.main()
