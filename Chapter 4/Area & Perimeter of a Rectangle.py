# Chp 4 Zelle, Programming Exercise 9

# Rectangle with two opposite points, area, & perimeter

from graphics import *

def main():

    print("This program draws a rectangle based on the user input")
    print("Of two mouse clicks")
    print("and then it computes the area and perimeter of the rectangle")
    print("In order to do this, we determine the")
    print("LENGTH based on the 'absolute value' of the change in X")
    print("and we determine the")
    print("WIDTH based on the 'absolue value' o the change in Y")
    print( )

    #creates the Graph, we are naming it win
    win = GraphWin("Rectangle, Area/Permiiter", 400,400)
    win.setCoords(0,0, 100,100)

    # gets the 1st & 2nd mouse clicks
    p1= win.getMouse()
    print("The 1st click is at Point: ", p1)

    p2 = win.getMouse()
    print("The 2nd click is at Point: ", p2)

    # draws a Rectangle
    rect = Rectangle(p1,p2)
    rect.draw(win)

    # ascribes x1,y1 and x2,y2 to mouse click one & mouse-click two
    x1 = p1.getX()
    y1 = p1.getY()

    x2 = p2.getX()
    y2 = p2.getY()

    # ascribes length based on the absolute value of the change in X
    # and ascribes width based on the absolute value of the change in Y

    length = abs(x2-x1)
    width = abs(y2-y1)

    area = length * width
    perimeter = 2 * (length + width)

    print("The length, or absolute value of the change in X, is: ", length)
    print("The width, or absolute value of the change in Y, is: ", width)

    print("The area of this rectangle is: ", area)
    print("The perimeter of this rectangle is: ", perimeter)
    print( )

main()

    





          
