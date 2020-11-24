# Zelle Chp 4, Exersise 2

# Bullseye Target

from graphics import *

def main():
    print("This program draws a bullseye target")
    print("creating 5 colorful circles")
    print("that overlap each other")

    win = GraphWin("BullsEye", 600, 600)
    win.setCoords(0,0,250,250)

    white = Circle(Point(125,125),100)
    white.setFill("white")
    white.setWidth(3)
    white.draw(win)

    black = Circle(Point(125,125),80)
    black.setFill("black")
    black.setWidth(3)
    black.draw(win)

    b = Circle(Point(125,125),60)
    b.setFill("blue")
    b.setWidth(3)
    b.draw(win)


    r = Circle(Point(125,125),40)
    r.setFill("red")
    r.setWidth(3)
    r.draw(win)

    y = Circle(Point(125,125),20)
    y.setFill("yellow")
    y.setWidth(3)
    y.draw(win)


    win.getMouse()
    win.close()
    

main()
