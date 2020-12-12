def main():
    print("This program illustrates a chaotic function")

    x = eval(input("Enter a number between 0 and 1: "))

    y = eval(input("Enter a number between 0 and 1: "))

    n = eval(input("How many numbers should I print? "))

    print("Index {0:>9}{1:>10}".format(x, y))

    print("--------------------")

    for i in range (n):
        x = 3.9* x * (1-x)
        y = 3.9* y * (1-y)
        print("{0:^3} {1:>12.6f} {2:>10.6f}".format((i+1),x,y)) 


main()
