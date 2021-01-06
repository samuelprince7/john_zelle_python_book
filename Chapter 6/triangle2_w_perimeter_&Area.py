# triangle2.py
# draws a triangle based on three clicks
# also calculates the perimeter & area based on built in fuctions


import math
from graphics import *

def square(x):
    return x**2

def distance(p1,p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def main():

    win = GraphWin("Draw a Triangle", 400, 400)

    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three points of a triangle

    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)


    # Use Polygon object to draw the triangle

    triangle = Polygon(p1,p2,p3)

    triangle.setFill("peachpuff")

    triangle.setOutline("cyan")

    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText("The perimeter is: {0:0.2f}".format(perim))

    def heron_tri_area(a, b, c):
        s = (a + b + c) / 2
        area = math.sqrt(s *(s-a) *(s-b) *(s-c))
        return area

    area = heron_tri_area(distance(p1,p2), distance(p2,p3), distance(p3,p1))

    message2 = Text(Point(5, 1.5), "The area is: {0:0.2f}".format(area))
    message2.draw(win)

    # Wait for another click to exit

    print("Side one is", distance(p1,p2))
    print("Side two is", distance(p2,p3))
    print("Side three is", distance(p3,p1))
    

    win.getMouse()
    win.close()

main()