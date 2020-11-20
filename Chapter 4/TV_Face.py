# Chp 4 Zelle, Programming Exercise #3

# Draw some sort of face

#I opted to make a TV face

from graphics import *

def main():

    print("This programs draws a TV looking face")

    win = GraphWin("TV Face",600,600)
    win.setCoords(0,0,25,25)

    face = Rectangle(Point(6,6), Point(18,18))
    face.setFill("red")
    face.setWidth(3)
    face.draw(win)

    mouth = Oval(Point(8,7), Point(16,10))
    mouth.setFill("yellow")
    mouth.setWidth(3)
    mouth.draw(win)

    eye1 = Circle(Point(9,15),1)
    eye1.setFill("yellow")
    eye1.setWidth(3)
    eye1.draw(win)

    eye2 = eye1.clone()
    eye2.draw(win)
    eye2.move(6,0)

    line1 = Line(Point(12,18), Point(16,22))
    line1.draw(win)

    line2 = Line(Point(12,18), Point(8,22))
    line2.draw(win)

    antena1 = Circle(Point(8,22),0.5)
    antena1.setFill("blue")
    antena1.draw(win)

    antena2 = antena1.clone()
    antena2.draw(win)
    antena2.move(8,0)

    win.getMouse()
    win.close()

main()
                 
