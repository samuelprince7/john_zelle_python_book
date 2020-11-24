# futval_graph2_easyCoords.py

from graphics import *

def main():

    #Introduction
    print("This program plots the growth of a 10-year investment.")

    #Create a graphics window w/labels on left edge

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    win.setCoords(-1.75,-5700, 11.5, 10400)

    Text(Point(-1,0), '0.0K').draw(win)
    Text(Point(-1,2500), '2.5K').draw(win)
    Text(Point(-1,5000), '5.0K').draw(win)
    Text(Point(-1,7500), '7.5K').draw(win)
    Text(Point(-1,10000), '10.0K').draw(win)

    Text(Point(2,-1000),"Enter Principal:").draw(win)
    Text(Point(2,-2700),"Enter APR:").draw(win)
    Text(Point(5,-4200),"Enter Principal,APR, then click screen").draw(win)

    inputPrincipal = Entry(Point(7,-1000), 5)
    inputPrincipal.setText("0.0")
    inputPrincipal.draw(win)

    inputAPR = Entry(Point(7,-2700), 5)
    inputAPR.setText("0.0")
    inputAPR.draw(win)

    # wait for a mouse click
    win.getMouse()

    principal = float(inputPrincipal.getText())
    apr = float(inputAPR.getText())



    # Draw bar for initial principal

    bar = Rectangle(Point(0,0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year

    for year in range(1,11):
        principal = principal * (1+apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

        

    win.getMouse()
    win.close()

main()

    
          
