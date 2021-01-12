#event_loop3
# handles the event of 'mouse clicks' inside of
# a box imported from the graphics modual 

from graphics import *

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    # create an Entry box for the user to type into

    entry = Entry(pt, 10)
    entry.draw(win)

    # Go modal: loop until user types <Enter> key 
    # using getKey() forces the user to go modal, meaning the program pauses and
    # nothing else will happen until the user presses the <Enter> key 
    # this is basically an infinate loop and
    # when the user presses a <Enter>, getKey() returns "Return" and the loop breaks

    while True:
        key = win.getKey()
        if key == "Return": break 

    # undraw the entry and create and draw Text0
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()

def main():
    win = GraphWin("Click and Type", 500, 500)
    # Event Loop: handle key presses and mouse clicks until the user 
    #  presses the "q" key.

    while True:
        key = win.checkKey()
        if key == "q":  #loop exit
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()

main()
    
