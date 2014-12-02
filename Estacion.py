from math import hypot
class Estacion():
	
	def __init__(self, nombre, transbordo, lineas_estaciones, punto):
		
		self.nombre = nombre
		self.transbordo = transbordo
		self.lineas_estaciones = lineas_estaciones
		self.punto = punto
		self.padre = None
		self.valor = 0
		self.g = 0
		
	def get_g(self, estacion):
		
		return hypot(estacion.punto.getX() - self.punto.getX(), estacion.punto.getY() - self.punto.getY())
	
		
