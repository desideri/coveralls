import unittest
#from Monopolio import Persona
from Celda import Celda
from Persona import Persona

class Test(unittest.TestCase):
    def test1(self):
		celda1 = Celda("Janina",1,"Propiedad",150,50,)
		persona1 = Persona("Cristina", 140)
        Msg = validar_movimiento(celda1,persona1)
        self.assertEquals(Msg,"Perdió")

    def test2(self):
        celda2 = Celda("Janina",1,"Propiedad",150,50)
		persona2 = Persona("Cristina", 160,"si")
        Msg = validar_movimiento(celda2,persona2)
        self.assertEquals(Msg,"Usted pagó renta")

    def test3(self)://Comprada por otros jugadores(N)
        celda3 = Celda("Janina",1,"Propiedad",150,50)
		persona3 = Persona("Sianna", 200,"si")
        Msg = validar_movimiento(celda3,persona3)
        self.assertEquals(Msg,"Usted ha comprado una propiedad")

    def test4(self):
        celda4 = Celda("",1,"Propiedad",150,50)
		persona4 = Persona("Cristina", 100,"si")
        Msg = validar_movimiento(celda4,persona4)
        self.assertEquals(Msg,"No tiene dinero suficiente")

    def test5(self): //No compra la popiedad pero tiene dinero
        celda5 = Celda("",1,"Propiedad",150,50,)
		persona5 = Persona("Juan", 300,"si")
        Msg = validar_movimiento(celda5,persona5)
        self.assertEquals(Msg,"Perdió")

    def test6(self):
        celda6 = Celda("Janina",1,"Propiedad",150,50)
		persona6 = Persona("Cristina", 140)
        Msg = validar_movimiento(celda6,persona6)
        self.assertEquals(Msg,"Usted ha comprado una propiedad")



if __name__ == '__main__':
    unittest.main()
