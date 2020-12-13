#futval.py
#   A program to compute the value of an investment
#   caried N years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Enter the number of years: "))

    print("{0:<8}{1:<13}".format("Year","Value"))

    print("---------------------------")

    for i in range(n+1):
        print("{0:^3}    ${1:7.2f}".format(i,principal))
        
        principal = principal * (1 + apr)
        
        

    
    print()

main()
    
