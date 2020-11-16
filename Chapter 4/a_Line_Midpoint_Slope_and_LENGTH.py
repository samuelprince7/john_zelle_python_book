# Chp 4 Zelle, Programming Exercise 8

# Circle Intersection

import math

from graphics import *

def main():

    print("This program draws a line segment based on two mouse clicks")
    print("then draws a point at the midpoint in cyan")
    print("It also prints the XY coordinates of both clicked points")
    print("the XY coordinates of the midpoint")
    print("the slope of the line")
    print("and perhaps most importantly, the LENGTH, of the line")


    #creates the Graph
    win = GraphWin("Line Segment w/Length & Midpoint Coordinates", 400, 400)
    win.setCoords(0, 0, 100, 100)

    # gets the 1st & 2nd mouse clicks
    p1 = win.getMouse()
    print("The 1st click is at Point: ", p1)

    p2 = win.getMouse()
    print("The 2nd click is at Point: ", p2)
    
    # ascribes x1,y1 and x2,y2 to mouse-click one and mouse-click two
    x1 = p1.getX()
    y1 = p1.getY()

    x2 = p2.getX()
    y2 = p2.getY()

    # sets value of the distance of points
    dx = x2 - x1
    dy = y2 - y1

    # creates the line itself
    L = Line(p1,p2)
    L.draw(win)

    # creates the midpoint in cyan
    midpoint = L.getCenter()
    midpoint.setFill("cyan")
    midpoint.draw(win)

    # calculates the slope and length of the line
    slope = dy / dx
    length = math.sqrt(dx**2 + dy**2)

    print("The midpoint is located at: ", midpoint)
    print("The slope of the line is: ", slope)
    print("The length of the line is: ", length)
    print("and you are awesome")

    print()

main()

    
    
    
          

