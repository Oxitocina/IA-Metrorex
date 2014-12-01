import math
class Algoritmo():
	
	def __init__(self, estaciones, origen, destino):
		self.estaciones = estaciones
		self.origen = origen
		self.destino = destino
		self.distHeur = {}
		for i in self.estaciones:
			distHeur[i.nombre] = math.hypot(destino.punto.getX() - i.punto.getX(), destino.punto.getY() - i.punto.getY())   
