# this program determines the cost of a pizza, per square inch.
#given its diameter and price.

def pizza():
    print("This program allows you to calculate how much your pizza costs, per square inch.")
    print("You will need to enter the total cost first, and then the Diameter of your pizza. Thank you.")

    print()

    cost = float(input("Enter the cost of your pizza: "))
    diameter = float(input("Enter the Diameter of your Pizza in inches: "))
    radius = diameter/2
    area = 3.14 * radius**2
    CPSI = cost / area

    print()
    print("The price per square inch is: " , CPSI )
    
    
pizza()
                 
