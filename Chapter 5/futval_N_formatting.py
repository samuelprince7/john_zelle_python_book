#futval.py
#   A program to compute the value of an investment
#   caried N years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Enter the number of years: "))

    y = "Year"
    v = "Value"
    print("{0:<8}{1:<13}".format(y,v))

    print("---------------------------")

    for i in range(n):
        principal = principal * (1 + apr)
        print("{0:^3}${1:>12.2f}".format((i),principal))

    
    print("The value in", n , "years is:", principal)

main()
    
