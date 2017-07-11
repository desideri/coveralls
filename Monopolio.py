class Persona:
  nombre = ""
  monto = 0
  comprar = ""
  def __init__(self, nombre, monto,comprar):
        self.nombre = nombre
        self.monto = monto
		self.comprar = comprar

class Celda:
  dueño = ""
  numero= 0
  tipo = ""
  precio = 0
  renta =  0
  def __init__(self, dueño, numero,tipo,precio,renta):
        self.dueño =  dueño
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.renta = renta

  def __str__(self):
        return self.dueño

def validar_movimiento(celda,turnoPersona):
  if (celda.tipo!="Propiedad"):
     # se ejecuta otro codigo
     print("la celda no es una Propiedad")
	 return "No Valido"
  else:
    if celda.dueño is "":
      if turnoPersona.monto < celda.precio:
        #sale del juego
        print("salio del juego")
		return "No tiene dinero suficiente"
      else:
		if turnoPersona.comprar=="si":
			#puede comprar
			print("paga para ser el dueño")
			turnoPersona.monto = turnoPersona.monto - celda.precio
			return "Usted ha comprado una propiedad"
		else:
			print("Sigue jugando")
			return "Sigue jugando"
    else:
      if celda.dueño == turnoPersona.nombre:
        #no pasa nada
        print("es el mismo dueño")
		return "Esta proiedad es suya"
      else:
        if turnoPersona.monto < celda.renta:
          #pierde el juego
          print("pierde el juego no tiene dinero para pagar")
		  return "Perdió"
        else:
          print("paga la renta")
          turnoPersona.monto = turnoPersona.monto - celda.renta
		  return "Usted pagó renta"
