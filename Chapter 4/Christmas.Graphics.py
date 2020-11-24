# Chp 4 Zelle, Programming Exercise #4

# Draw a winter scene with a tree and snowman

from graphics import *

def main():

    print("This programs draws a Christmas Tree & Snowman")

    win = GraphWin("Christmas",600,600)
    win.setCoords(0,0,25,25)

    foundation = Line(Point(0,2), Point(25,2))
    foundation.draw(win)

    # the Tree

    base = Rectangle(Point(6,2), Point(8,6))
    base.setFill("green")
    base.setOutline("green")
    base.draw(win)

    p1 = Point(1,6)
    p2 = Point(13,6)
    p3 = Point(7,12)
    p4 = Point(1,9)
    p5 = Point(13,9)
    p6 = Point(7,16)
    p7 = Point (2,12)
    p8 = Point(12,12)
    p9 = Point(7,18)
    p10 = Point(3,15)
    p11 = Point(11,15)
    p12 = Point(7,20)

    tri1 = Polygon(p1,p2,p3)
    tri1.setFill("green")
    tri1.setOutline("green")
    tri1.draw(win)

    tri2 = Polygon(p4,p5,p6)
    tri2.setFill("green")
    tri2.setOutline("green")
    tri2.draw(win)    

    tri3 = Polygon(p7,p8,p9)
    tri3.setFill("green")
    tri3.setOutline("green")
    tri3.draw(win)       

    tri4 = Polygon(p10,p11,p12)
    tri4.setFill("green")
    tri4.setOutline("green")
    tri4.draw(win)         

    # the Snowman
    snow_ball1 = Circle(Point(19,6), 4)
    snow_ball1.setFill("white")
    snow_ball1.draw(win)

    snow_ball2 = Circle(Point(19, 12.5), 3.5)
    snow_ball2.setFill("white")
    snow_ball2.draw(win)

    snow_ball3 = Circle(Point(19,18), 2)
    snow_ball3.setFill("white")
    snow_ball3.draw(win)

    mouth = Oval(Point(18.25,16.5), Point(19.75,17.5))
    mouth.draw(win)

    eye1 = Circle(Point(18.5,19), 0.25)
    eye1.setFill("black")
    eye1.draw(win)

    eye2 = eye1.clone()
    eye2.draw(win)
    eye2.move(1,0)

    #draws the snowmans arms as lines

    line1 = Line(Point(18,14), Point(14,15))
    line1.draw(win)

    line2 = Line(Point(13,16), Point(14,15))
    line2.draw(win)

    line3 = Line(Point(12,15), Point(14,15))
    line3.draw(win)

    line4 = Line(Point(20,14), Point(23,16))
    line4.draw(win)

    line5 = Line(Point(23.5,17), Point(23,16))
    line5.draw(win)

    line6 = Line(Point(24,16.5), Point(23,16))
    line6.draw(win)

    win.getMouse()
    win.close()

main()









    





