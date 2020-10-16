# this program demonstrates how computers store numbers.
# specifically, algebracially equivalent equations produce different values
# when they are processed by a computer, than if the equation is processed by human hands.

# EXAMPLE 
# 3.9 * x * (1 - x)  IS ALGEBRACIALLY EQUIVALENT TO 3.9 * (x - x * x)
# 3.9 * x * (1 - x)  IS ALGEBRACIALLY EQUIVALENT TO 3.9 * x - 3.9 * x * x

# however, if you run the program with the two alternative algebraical equations above
# and set n = 100
# you will find at a certain point, the equations produce different results.

# this is mainly due to the way in which computers store numerical data 


def main():
    print("This program illustrates a chaotic function")
    x=eval(input("Enter a number between 0 and 1: "))
    n=eval(input("How many numbers should I print? "))
    for i in range (n):
        x=3.9* x * (1-x)
        print(x)


main()
