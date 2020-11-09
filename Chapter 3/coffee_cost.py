def coffee_cost():

    print("This program finds the total cost of an oder of coffee")
    print("that is $10.50 per pound, plus the cost of shipping")
    print("which is $0.86 per pound + a flat fee of $1.50 fixed cost")
    print("for general overhead")

    pounds = float(input("How many pounds of coffee would you like to buy?: "))

    cost = pounds * 10.50

    shipping = pounds * 0.86

    cost_with_shipping = cost + shipping

    total_cost = cost_with_shipping + 1.50

    print("The total cost of ", pounds, "pounds of coffee is $", total_cost )

coffee_cost()
