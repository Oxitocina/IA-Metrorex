class Estacion():
	
	def __init__(self, nombre, transbordo, lineas_estaciones, punto):
		
		self.nombre = nombre
		self.transbordo = transbordo
		self.lineas_estaciones = lineas_estaciones
		self.punto = punto
		self.padre = None
		self.valor = 0
		
	
		
