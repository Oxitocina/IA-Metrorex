from graphics import *
from Algoritmo import *
from Estacion import *

def main():
    ventana = GraphWin("Metro", 1044, 762)
    image = Image(Point(522,381),"harta-metrou.png")
    image.draw(ventana)
    puntos = {"Pantelimon": (933, 394.5), "Republica": (840, 415.5), "Costin": (813, 450), "Titan": (784.5, 486),
				"Nicolae": (759, 520.5), "Dristor": (682.5, 504), "Muncii": (684, 447), "Lancului":(682, 388.5),
				"Obor": (627, 361.5), "Stefan": (565, 332.5), "Victoriei": (502.5, 309), "Gara": (450, 273),
				"Basarab": (415.5, 255), "Crangasi": (367.5, 294), "Petrache": (327, 333), "Grozavesti": (384, 367.5),
				"Eroilor": (433.5, 403.5), "Izvor": (493.5, 435), "Unirii": (546, 459), "Timpuri": (598.5, 514.5),
				"Mihai": (637.5, 553.5), "Anghel": (970.5,571.5), "Teclu": (895.5,558), "1918": (822, 540), 
				"Politehnica": (358.5, 420), "Lujerului": (286.5, 433.5), "Gorjului": (217.5, 447), "Pacii": (150, 460.5),
				"Preciziei": (85.5, 471), "Berceni": (711, 726), "Dimitrie": (669, 696), "Patriei": (634.5, 670.5), 
				"Sudului": (598.5, 643.5), "Constantin": (561, 616.5), "Eroii": (556.5, 564), "Tineretului": (555, 510), 
				"Universitate": (535.5, 409.5), "Romana": (516, 366), "Aviatorilor": (520.5, 246), "Aurel": (544.5, 180), 
				"Pipera": (598.5, 141), "Grivita": (382.5, 231), "Mai": (342, 211.5), "Pajura": (315, 195),
				"Parc": (288, 181), "Laminorului": (258, 163.5)}
	
    circulos = []
    estaciones = [Estacion("Anghel", 0, {"3":("Teclu", None)}, (970.5,571.5)), Estacion("Teclu", 0, {"3":("Anghel", "1918")}, (895.5,558)),
					Estacion("1918", 0, {"3":("Nicolae","Teclu")}, (822, 540)),Estacion("Nicolae", 100, {"3":("Dristor","1918"),"1":("Dristor", "Titan")}, (759, 520.5)),
					 Estacion("Dristor", 200, {"3":("Nicolae", "Mihai"), "1":("Nicolae", "Mihai", "Muncii")},(682.5, 504)),
					 Estacion("Mihai", 0, {"1":("Dristor", "Timpuri"), "3":("Dristor", "Timpuri")},(637.5, 553.5)),
					 Estacion("Timpuri", 0, {"1":("Mihai", "Unirii"), "3":("Mihai", "Unirii")}, (598.5, 514.5)),
					 Estacion("Unirii", 300, {"1":("Izbor", "Timpuri"), "2": ("Universitate", "Tineretului"), "3":("Izbor", "Timpuri")},  (546, 459)),
					 Estacion("Izbor", 0, {"1":("Eroilor", "Unirii"), "3":("Eroilor", "Unirii")}, (493.5, 435)),
					 Estacion("Eroilor", 400, {"1":("Grozavesti", "Izbor"), "3":("Politehnica", "Izbor")}, (433.5, 403.5)),
					 Estacion("Politehnica", 0, {"3":("Eroilor", "Lujerului")},(358.5, 420)),
					 Estacion("Lujerului", 0, {"3":("Gorjului", "Politehnica")},(286.5, 433.5)),
					 Estacion("Gorjului", 0, {"3":("Lujerului", "Pacii")},(217.5, 447)),
					 Estacion("Pacii", 0, {"3":("Preciziei", "Gorjului")},(150, 460.5)), Estacion("Preciziei", 0, {"3":("Pacii", None)},(85.5, 471)),
					 Estacion("Pantelimon", 0, {"1":("Republica", None)}, (933, 394.5)), Estacion("Republica", 0, {"1":("Pantelimon", "Costin")}, (840, 415.5)),
					 Estacion("Costin", 0, {"1":("Republica", "Titan")}, (813, 450)), Estacion("Titan", 0, {"1":("Nicolae", "Costin")},(784.5, 486)),
					 Estacion("Muncii", 0, {"1":("Dristor", "Lancului")},(684, 447)), Estacion("Lancului", 0, {"1":("Muncii", "Obor")},(682, 388.5)),
					 Estacion("Obor", 0, {"1":("Stefan", "Lancului")},(627, 361.5)), Estacion("Stefan", 0, {"1":("Victoriei", "Obor")},(565, 332.5)),
					 Estacion("Victoriei", 500, {"1":("Stefan", "Gara"), "2": ("Romana", "Aviatorilor")},(502.5, 309)),
					 Estacion("Gara", 600, {"1":("Victoriei", "Basarab"), "4": ("Basarab", None)},(450, 273)),
					 Estacion("Basarab", 0, {"1":("Crangasi", "Gara"), "4": ("Gara", "Grivita")}, (415.5, 255)),
					 Estacion("Crangasi", 0, {"1":("Basarab", "Petrache")},(367.5, 294)), Estacion("Petrache", 0, {"1":("Crangasi", "Grozavesti")},(327, 333)),
					 Estacion("Grozavesti", 0, {"1":("Eroilor", "Petrache")},(384, 367.5)),Estacion("Berceni", 0, {"2":("Dimitrie", None)},(711, 726)),
					 Estacion("Dimitrie", 0, {"2":("Berceni", "Patriei")},(669, 696)), Estacion("Patriei", 0, {"2":("Dimitrie", "Sudului")},(634.5, 670.5)),
					 Estacion("Sudului", 0, {"2":("Constantin", "Patriei")},(598.5, 643.5)), Estacion("Constantin", 0, {"2":("Eroii", "Sudului")},(561, 616.5)),
					 Estacion("Eroii", 0, {"2":("Constantin", "Tiniretului")},(556.5, 564)), Estacion("Tineretului", 0, {"2":("Eroii", "Unirii")},(555, 510)),
					 Estacion("Universitate", 0, {"2":("Unirii", "Romana")},(535.5, 409.5)), Estacion("Romana", 0, {"2":("Universitate", "Victoriei")}, (516, 366)),
					 Estacion("Aviatorilor", 0, {"2":("Aurel", "Victoriei")}, (520.5, 246)), Estacion("Aurel",0, {"2": ("Aviatorilor", "Pipera")}, (544.5, 180)),
					 Estacion("Pipera", 0, {"2":("Aurel", None)}, (598.5, 141)), Estacion("Grivita", 0, {"4": ("Basarab", "Mai")},(382.5, 231)),
					 Estacion("Mai", 0, {"4": ("Grivita", "Pajura")},(342, 211.5)), Estacion("Pajura", 0, {"4": ("Parc", "Mai")},(315, 195)),
					 Estacion("Parc", 0, {"4": ("Laminorului", "Pajura")},(288, 181)), Estacion("Laminorului", 0, {"4":("Parc", None)}, (258, 163.5))]
					 
    for i in puntos.values():
        circulos.append(Circle(Point(i[0],i[1]),6.5))
    c = Circle(Point(515.5,365.5), 6.5)
    c.draw(ventana)
    for i in circulos:
        i.setOutline("#33FF00")
        i.setWidth("3")
        #i.draw(ventana)
    bien = False
    while not bien:
        bien = True
        try:
            comienzo = ventana.getMouse()
            circulo_inicio, estacion_inicio = ranguizador(circulos, estaciones, comienzo)
            circulo_inicio.draw(ventana)
        except AttributeError:
            bien = False
    bien = False
    while not bien:
        bien = True
        try:
            final = ventana.getMouse()
            circulo_final, estacion_final = ranguizador(circulos, estaciones, final)
            circulo_final.draw(ventana)
        except AttributeError:
            bien = False
    if len(estacion_inicio.lineas_estaciones.items()) > 1:
        linea = input("Introduzca la linea por la que desea entrar (" + str(list(estacion_inicio.lineas_estaciones.keys())) + "): ")
    else:
        linea = list(estacion_inicio.lineas_estaciones.keys())[0]
    
    lets_go = Algoritmo(estaciones, estacion_inicio, estacion_final, linea)
    lets_go.paso_1()
    camino = lets_go.camino_al_destino()
    print (camino)
    for i in range(0,len(camino)-1):
        linea = Line(Point(camino[i][0], camino[i][1]), Point(camino[i+1][0], camino[i+1][1]))
        linea.setOutline("#33FF00")
        linea.setWidth("5")
        linea.draw(ventana)
    
    ventana.getMouse() 
    ventana.close() 
def ranguizador(circulos, estaciones, punto):
	rango = ((punto.getX()-6.5, punto.getX()+6.5), (punto.getY()-6.5, punto.getY()+6.5))
	circulo = None
	estacion = None
	for i in circulos:
		if i.getCenter().getX()>=rango[0][0] and i.getCenter().getX()<=rango[0][1] and i.getCenter().getY()>=rango[1][0] and i.getCenter().getY()<=rango[1][1]:
			circulo = i
	for j in estaciones:
		if j.punto[0]>=rango[0][0] and j.punto[0]<=rango[0][1] and j.punto[1]>=rango[1][0] and j.punto[1]<=rango[1][1]:
			estacion = j
	return circulo, estacion
		 
main()
