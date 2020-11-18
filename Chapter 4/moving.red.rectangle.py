# Chapter 4 , Discussion #3

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(35,65), Point(55,85))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)

    win.close()

main()
        
