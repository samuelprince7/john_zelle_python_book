def distance():

    import math
    
    print("This program determines the distance of two points.")
    print("Based on the input of two coordinate points in x,y format.")

    print()

    x1, y1 = eval(input("Enter the x,y coordinate of the BEGINNING point of the line seperated by a comma: "))
    x2, y2 = eval(input("Enter the x,y coordinate of the FINISHING point of the line seperated by a comma: "))

    distance = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

    print("The distance, between the coordinates that you entered, is: ", distance)

distance()
