from graphics import *
from Estacion import *

def main():
    ventana = GraphWin("Metro", 1044, 762)
    image = Image(Point(522,381),"harta-metrou.png")
    image.draw(ventana)
    puntos = {"Pantelimon": (933, 394.5), "Republica": (840, 415.5), "Costin": (813, 450), "Titan": (784.5, 486),
				"Nicolae": (759, 520.5), "Dristor": (682.5, 504), "Muncii": (684, 447), "Lancului":(682, 388.5),
				"Obor": (627, 361.5), "Stefan": (565.5, 333), "Victorei": (502.5, 309), "Gara": (450, 273),
				"Basarab": (415.5, 255), "Crangasi": (367.5, 294), "Petrache": (327, 333), "Grozavesti": (384, 367.5),
				"Eroilor": (433.5, 403.5), "Izvor": (493.5, 435), "Unirii": (546, 459), "Timpuri": (598.5, 514.5),
				"Mihai": (637.5, 553.5), "Anghel": (970.5,571.5), "Teclu": (895.5,558), "1918": (822, 540), 
				"Politehnica": (358.5, 420), "Lujerului": (286.5, 433.5), "Gorjului": (217.5, 447), "Pacii": (150, 460.5),
				"Preciziei": (85.5, 471), "Berceni": (711, 726), "Dimitrie": (669, 696), "Patriei": (634.5, 670.5), 
				"Sudului": (598.5, 643.5), "Constantin": (561, 616.5), "Eroii": (556.5, 564), "Tineretului": (555, 510), 
				"Universitate": (535.5, 409.5), "Romana": (516, 366), "Aviatorilor": (520.5, 246), "Aurel": (544.5, 180), 
				"Pipera": (598.5, 141), "Grivita": (382.5, 231), "Mai": (342, 211.5), "Pajura": (289.5, 181.5),
				"Parc": (315, 195), "Laminorului": (258, 163.5)}
	
    circulos = []
    estaciones = [] #Chaparselo a mano
    for i in puntos.values():
        circulos.append(Circle(Point(i[0],i[1]),6.5))
    c = Circle(Point(515.5,365.5), 6.5)
    c.draw(ventana)
    for i in circulos:
        i.setOutline("red")
        i.setWidth("3")
        #i.draw(ventana)
    comienzo = ventana.getMouse()
    
    estacion_inicio = ranguizador(circulos, comienzo)
    estacion_inicio.draw(ventana)
    final = ventana.getMouse()
    estacion_final = ranguizador(circulos, final)
    estacion_final.draw(ventana)
    
    ventana.getMouse() 
    ventana.close() 
def ranguizador(circulos, punto):
	rango = ((punto.getX()-6.5, punto.getX()+6.5), (punto.getY()-6.5, punto.getY()+6.5))
	for i in circulos:
		if i.getCenter().getX()>=rango[0][0] and i.getCenter().getX()<=rango[0][1] and i.getCenter().getY()>=rango[1][0] and i.getCenter().getY()<=rango[1][1]:
			return i 
main()
