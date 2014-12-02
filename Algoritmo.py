import math
from Estacion import *
class Algoritmo():
	
	def __init__(self, estaciones, origen, destino, linea):
		self.estaciones = estaciones
		self.origen = origen
		self.destino = destino
		self.linea_actual = linea
		self.distHeur = {}
		self.abierta = [origen]
		self.cerrada = []
		for i in self.estaciones:
			distHeur[i.nombre] = math.hypot(destino.punto.getX() - i.punto.getX(), destino.punto.getY() - i.punto.getY())
			
	def paso_1(self):
		if len(self.cerrada) == 0:
			self.origen.valor = distHeur[origen.nombre]
			#igual no
		else:
			papito=self.cerrada[len(cerrada)-1]
			for i in papito.lineas_estaciones.items():
				for n in i[1]:
					for j in self.estaciones:
						if n == j.nombre:
							if not j in self.abierta:
								abierta.append(j)
								j.padre=papito
								j.valor = calcular_valor(j)
								if i[0] != self.linea_actual:
									j.valor += j.padre.transbordo
							else:
								a = calcular_valor(j)
								if a < j.valor:
									j.valor = a
									j.padre = papito
		self.paso_2()
	
	def paso_2(self):
		minimo = self.abierta[0]
		for i in self.abierta:
			if i.valor < minimo.valor:
				minimo = i
		cerrada.append[i]
		abierta.remove(i)
		if i.nombre != destino.nombre:
			self.paso_1()		
								
	def camino(self):
		resultado = [self.cerrada[len(cerrada)-1].punto]
		actual = self.cerrada[len(cerrada)-1]
		while actual.nombre != origen.nombre:
			resultado.append(actual.padre.punto)
			actual = actual.padre
		return resultado
		
	def calcular_valor(self, estacion):
		
		return estacion.padre.g + estacion.get_g(estacion.padre) + distHeur[estacion.nombre]
