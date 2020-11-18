# Chp 4 Zelle, Programming Exercise 10

# Triangle from 3 clicks, the length of each line

# as well as the perimeter & area of the triangle

import math

from graphics import *

def main():

    print("This program draws a triangle based on 3 mouse clicks")
    print("it then determines the length from click 1 to click 2 as line A")
    print("then determines the length from click 2 to click 3 as line B")
    print("then determines the length from click 3 to click 1 as line C")
    print()
    print("then...based on that data itself..")
    print("we easily compute the perimeter and area of the triangle")

    #creates the Graph
    win = GraphWin("Triangle A,B,C |Area|Perm", 400, 400)
    win.setCoords(0, 0, 100, 100)

    # gets the 1st, 2nd & 3rd mouse clicks
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    # draws triangle

    tri = Polygon(p1,p2,p3)
    tri.draw(win)

    # ascribes x1,y1 and x2,y2 and x3,y3 to mouse-click 1,2 and 3
    x1 = p1.getX()
    y1 = p1.getY()

    x2 = p2.getX()
    y2 = p2.getY()

    x3 = p3.getX()
    y3 = p3.getY()

    # computes the length of line a, b, and c

    dxa = x2 - x1
    dya = y2 - y1
    length_a = math.sqrt(dxa**2 + dya**2)

    dxb = x3 - x2
    dyb = y3 - y2
    length_b = math.sqrt(dxb**2 + dyb**2)

    dxc = x1 - x3
    dyc = y1 - y3
    length_c = math.sqrt(dxc**2 + dyc**2)

    # computes triangle Perimeter

    perimeter = length_a + length_b + length_c

    # computes triangle Area

    s = perimeter / 2

    area = math.sqrt(s * (s-length_a) * (s-length_b) * (s-length_c))

    # prints the length of line a,b,c and perimeter and length

    print("the length of click 1 to click 2")
    print(" or line A is: ", length_a)

    print("the length of click 2 to click 3")
    print(" or line B is: ", length_b)

    print("the length of click 3 to click 1")
    print(" or line C is: ", length_c)

    print("The Perimeter of the Triangle is: ", perimeter)
    print("The Area of the Triangle is: ", area)
    print()

main()
    
    

    
