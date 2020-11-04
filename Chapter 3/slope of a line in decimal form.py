def main():
    print("This program determines the slope of a line.")
    print("Based on the input of a BEGINNING coordinate in x,y format.")
    print("and on the input of a second FINISHING coordinate in x,y format.")

    print()

    x1, y1 = eval(input("Enter the x,y coordinate of the BEGINNING point of the line seperated by a comma: "))
    x2, y2 = eval(input("Enter the x,y coordinate of the FINISHING point of the line seperated by a comma: "))

    slope = (y2-y1)/(x2-x1)

    print("The slope of the line, based on the coordinates that you entered, is: ", slope)

main()
          
