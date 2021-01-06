# this program determines the cost of a pizza, per square inch.
#given its diameter and price.

def pizza():
    print("This program allows you to calculate how much your pizza costs, per square inch.")
    print("You will need to enter the total cost first, and then the Diameter of your pizza. Thank you.")

    print()

    pizza_cost = float(input("Enter the cost of your pizza: "))
    pizza_diameter = float(input("Enter the Diameter of your Pizza in inches: "))
    pizza_radius = pizza_diameter/2

    def pizza_area(radius):
        area = 3.14 * radius**2
        return area

    def cost_per_sq_in(cost, area):
        CPSI = cost / area
        return CPSI 

    a = pizza_area(pizza_radius)
    b = cost_per_sq_in(pizza_cost, a)

    print()
    print("The pizza's area is {0:0.2f} square inches, and it's cost per sq inch is {1:0.2f} .".format(a,b)) 
    
pizza()
                 