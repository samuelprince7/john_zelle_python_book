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
        x1= p.getX()
        y1 = p.getY()
        new_square = Rectangle(Point(x1,y1), Point(x1+20, y1+20))
        new_square.draw(win)

    win.close()

main()
        
