import math
from Estacion import *
class Algoritmo():
	
	def __init__(self, estaciones, origen, destino, linea):
		self.estaciones = estaciones
		self.origen = origen
		self.destino = destino
		self.linea_actual = linea
		self.cosas_a_cambiar = []
		self.distHeur = {}
		self.abierta = [origen]
		self.cerrada = []
		for i in self.estaciones:
			self.distHeur[i.nombre] = math.hypot(destino.punto[0] - i.punto[0], destino.punto[1] - i.punto[1])
			
	def paso_1(self):
		
		print("paso1")
		print ("Cerrada: ", end = "")
		for p in self.cerrada: 
			print(p.nombre, p.valor,end =" ")
		print ("\nAbierta: ", end = "")
		for p in self.abierta: 
			print( p.nombre, p.valor,end =" ")
		print("")
		if len(self.cerrada) == 0:
			print("primera iteracion")
			self.origen.valor = self.distHeur[self.origen.nombre]
			#igual no
		else:
			papito=self.cerrada[len(self.cerrada)-1]
			print(papito.nombre)
			for i in papito.lineas_estaciones.items():
				if i[0] != self.linea_actual and papito.transbordo == 0:
					print("linea "+ i[0] + " no accesible")
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
							print("estudiando el nodo " + n + " con resultado " + str(bien))
							print ("antes calc valor")
							print ("Cerrada: ", end = "")
							for p in self.cerrada: 
								print(p.nombre, p.valor, end =" ")
							print ("\nAbierta: ", end = "")
							for p in self.abierta: 
								print( p.nombre, p.valor,end =" ")
							print("")
							if bien == 0:
								print ("nodo no en abierta o cerrada")
								self.abierta.append(j)
								j.padre=papito
								j.valor = self.calcular_valor(j)
								if i[0] != self.linea_actual:
									print("Transbordo" + str(j.padre.transbordo))
									j.valor += j.padre.transbordo
									print ("valor: " + str(j.valor))
									self.cosas_a_cambiar.append( (i[0], j.nombre) )
							elif bien == 1:
								print ("Nodo en abierta(recalculo")
								print ("Abierta: ", end = "")
								for p in self.abierta: 
									print( p.nombre, p.valor, end =" ")
								print("")
								a = self.calcular_valor(j)
								if a < j.valor:
									j.valor = a
									j.padre = papito
									if i[0] != self.linea_actual:
										print("Transbordo" + str(j.padre.transbordo))
										j.valor += j.padre.transbordo
										print ("valor: " + str(j.valor))
										self.cosas_a_cambiar.append( (i[0], j.nombre) )
		print ("despues calc valor")
		print ("Cerrada: ", end = "")
		for p in self.cerrada: 
			print(p.nombre, p.valor, end =" ")
		print ("\nAbierta: ", end = "")
		for p in self.abierta: 
			print( p.nombre, p.valor, end =" ")
		print("")
		self.paso_2()
	
	def paso_2(self):
		print ("paso2")
		minimo = self.abierta[0]
		for i in self.abierta:
			if i.valor < minimo.valor:
				minimo = i
		if self.cosas_a_cambiar:
			for culo in self.cosas_a_cambiar:
				if culo[1] == minimo.nombre:
					self.linea_actual = culo[0]
			self.cosas_a_cambiar = []
		if minimo.padre != None:	
			minimo.g = minimo.padre.g + minimo.get_g(minimo.padre)
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
		print(estacion.padre.nombre)
		print ("la distancia padre-hijo es " + str(estacion.get_g(estacion.padre)))
		print ("la distancia heuristica es " + str(self.distHeur[estacion.nombre]))
		print ("la distancia acumulada es " + str(estacion.padre.g))
		return estacion.padre.g + estacion.get_g(estacion.padre) + self.distHeur[estacion.nombre]
