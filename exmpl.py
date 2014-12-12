from graphics import *
CONFIG = {"fill":"",
      "outline":"red",
      "width":"3",
      "arrow":"none",
      "text":"",
      "justify":"center",
                  "font": ("helvetica", 12, "normal")}
def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(50,90), 10)
    d = Circle(Point(70,90),10)
    e = Oval(Point(60,80),Point(60,20))
    line = Line(Point(200,200),Point(250,250))
    image = Image(Point(500,400),"harta-metrou.png")
    e.setOutline("red")
    line.setWidth("3")
    image.draw(win)
    c.draw(win)
    d.draw(win)
    e.draw(win)
    line.draw(win)
    rectangulo = Rectangle(Point(100,200), Point(500,400))
    rectangulo.setFill("Grey")
    rectangulo.draw(win)
    pene2 = Text(Point(300,250), "Introduzca la linea por la que desea entrar (" + str(list(estacion_inicio.lineas_estaciones.keys())) + "): ")
    pene2.draw(win)
    hola = Entry(Point(300,300), 25)
    hola.setFill("White")
    hola.draw(win)
    rectangulo2 = Rectangle(Point(260,340), Point(350,370))
    rectangulo2.setFill("Grey")
    rectangulo2.draw(win)
    pene3 = Text(Point(305,355), "Aceptar")
    pene3.draw(win)
    win.getMouse()
    pene = Text(Point(500,500), hola.getText())
    pene.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
