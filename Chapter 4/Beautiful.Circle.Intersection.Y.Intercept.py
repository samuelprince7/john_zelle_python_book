# Chp 4 Zelle, Programming Exercise 7

# Circle Intersection

from graphics import *

import math 

def main():

    print("This program draws a circle (given user input of the radius")
    print("and then draws a horizontal line through the circle based")
    print("on the user entering the y intercept of the line")
    print("and then it will draw the two x intercept points along the circle")
    print("as red dots...and it will also print both of the x coordinate values")
    print()

    #creates the Graph
    win = GraphWin("Circle,Line,X1/X2", 400, 400)
    win.setCoords(-10,-10, 10, 10)

    #requests user input
    r = float(input("Enter the radius of the circle: "))
    y = float(input("Enter the Y axis of the horizontal line: "))

    # draw a line from point(-10,y) to point (10,y)
    l = Line(Point(-10,y), Point(10,y))
    l.draw(win)

    # draws a circle w/center at (0,0) based on user input of radius
    c = Circle(Point(0,0), r)
    c.draw(win)

    # calculate the +x intercept and the -x intercept of the horizontal circle and line
    x1 = (1) * math.sqrt(r**2 - y**2)
    x2 = (-1) * math.sqrt(r**2 - y**2)

    # creates the +x point and the -x point on the graph as Red Dots

    p1 = Point(x1,y)
    p1.setFill("red")
    p1.draw(win)

    p2 = Point(x2,y)
    p2.setFill("red")
    p2.draw(win)

    x1 = round(x1,2)
    x2 = round(x2,2)

    print()
    print("The value of the +X coordinate is:", x1)
    print("The value of the -X coordinate is:", x2)

main()
    



    

    
    

    

    
