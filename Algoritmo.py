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
			self.distHeur[i.nombre] = math.hypot(destino.punto[0] - i.punto[0], destino.punto[1] - i.punto[1])
			
	def paso_1(self):
		print("paso1")
		#print (x: self.cerrada)
		print (self.abierta)
		if len(self.cerrada) == 0:
			print("primera iteracion")
			self.origen.valor = self.distHeur[self.origen.nombre]
			#igual no
		else:
			papito=self.cerrada[len(self.cerrada)-1]
			print(papito.nombre)
			for i in papito.lineas_estaciones.items():
				if i[0] != self.linea_actual and papito.transbordo == 0:
					print("transbordo")
					continue
				for n in i[1]:
					for j in self.estaciones:
						if n == j.nombre:
							bien = 0
							
							for x in self.abierta:	
								if j.nombre == x.nombre:
									bien = 1
									break
							for y in self.cerrada:
								if j.nombre == y.nombre:
									bien = 2
									break
							print ("antes calc valor")
							print (self.cerrada)
							print (self.abierta)
							if bien == 0:
								print ("culero")
								self.abierta.append(j)
								j.padre=papito
								j.valor = self.calcular_valor(j)
								if i[0] != self.linea_actual:
									print("pito")
									j.valor += j.padre.transbordo
									self.linea_actual = i[0]
							elif bien == 1:
								print ("culo")
								print (self.abierta)
								a = self.calcular_valor(j)
								if a < j.valor:
									j.valor = a
									j.padre = papito
		print ("despues calc valor")
		print (self.cerrada)
		print (self.abierta)
		self.paso_2()
	
	def paso_2(self):
		print ("paso2")
		minimo = self.abierta[0]
		for i in self.abierta:
			if i.valor < minimo.valor:
				minimo = i
		self.cerrada.append(minimo)
		self.abierta.remove(minimo)
		if minimo.nombre != self.destino.nombre:
			self.paso_1()		
								
	def camino_al_destino(self):
		resultado = [self.cerrada[len(self.cerrada)-1].punto]
		actual = self.cerrada[len(self.cerrada)-1]
		while actual.nombre != self.origen.nombre:
			resultado.append(actual.padre.punto)
			actual = actual.padre
		return resultado
		
	def calcular_valor(self, estacion):
		print(estacion.padre)
		return estacion.padre.g + estacion.get_g(estacion.padre) + self.distHeur[estacion.nombre]
