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
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
