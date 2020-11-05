def lightning():
    print("This program determines the distance in miles")
    print("to a lightning strike")
    print("based on the number of seconds")
    print("elapsed between the flash & the sound of thunder.")

    seconds = float(input("How many seconds passed between seeing LIGHTning and the sound of thunder?: "))

    distance_in_miles = (seconds * 1100) / 5280

    print()
    print("The distance to the lightning strike in miles is:", distance_in_miles )

lightning() 

    
