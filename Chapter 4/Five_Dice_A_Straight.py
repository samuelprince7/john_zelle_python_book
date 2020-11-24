# Chp 4 Zelle, Programming Exercise #5

# Draw a 5 dice depicting a straight 

from graphics import *

def main():

    print("This programs draws a set of dice depicting a straight")

    win = GraphWin("Dice Straight",600,600)
    win.setCoords(0,0,125,125)

    die1 = Rectangle(Point(5,10), Point(35,40))
    die1.setWidth(2)
    die1.draw(win)

    dot1_1 = Circle(Point(20,25), 1)
    dot1_1.setFill("black")
    dot1_1.draw(win) 

    die2 = Rectangle(Point(45,10), Point(75,40))
    die2.setWidth(2)
    die2.draw(win)

    dot2_1 = Circle(Point(50,35), 1)
    dot2_1.setFill("black")
    dot2_1.draw(win) 

    dot2_2 = Circle(Point(70,15), 1)
    dot2_2.setFill("black")
    dot2_2.draw(win) 

    die3 = Rectangle(Point(90,10), Point(120,40))
    die3.setWidth(2)
    die3.draw(win)

    dot3_1 = Circle(Point(95,35), 1)
    dot3_1.setFill("black")
    dot3_1.draw(win) 

    dot3_2 = Circle(Point(105,25), 1)
    dot3_2.setFill("black")
    dot3_2.draw(win) 

    dot3_3 = Circle(Point(115,15), 1)
    dot3_3.setFill("black")
    dot3_3.draw(win) 

    die4 = Rectangle(Point(20,70), Point(50,100))
    die4.setWidth(2)
    die4.draw(win)

    dot4_1 = Circle(Point(25,95), 1)
    dot4_1.setFill("black")
    dot4_1.draw(win) 

    dot4_2 = Circle(Point(25,75), 1)
    dot4_2.setFill("black")
    dot4_2.draw(win) 

    dot4_3 = Circle(Point(45,95), 1)
    dot4_3.setFill("black")
    dot4_3.draw(win) 

    dot4_4 = Circle(Point(45,75), 1)
    dot4_4.setFill("black")
    dot4_4.draw(win) 

    die5 = Rectangle(Point(70,70), Point(100,100))
    die5.setWidth(2)
    die5.draw(win)

    dot5_1 = Circle(Point(75,95), 1)
    dot5_1.setFill("black")
    dot5_1.draw(win) 

    dot5_2 = Circle(Point(75,75), 1)
    dot5_2.setFill("black")
    dot5_2.draw(win) 

    dot5_3 = Circle(Point(85,85), 1)
    dot5_3.setFill("black")
    dot5_3.draw(win) 

    dot5_4 = Circle(Point(95,75), 1)
    dot5_4.setFill("black")
    dot5_4.draw(win) 

    dot5_5 = Circle(Point(95,95), 1)
    dot5_5.setFill("black")
    dot5_5.draw(win) 


    win.getMouse()
    win.close()

main()


