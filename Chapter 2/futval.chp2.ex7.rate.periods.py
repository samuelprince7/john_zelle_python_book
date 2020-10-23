# futval.py
#       exersise 7
#    A program to compute the future value of an investment
#    with number of years set to ten

# AND the yearly rate determined by the user (rate)
# AND the number of times the interest is compounded (periods)determined by the user


def main():
    print("This program calculates the total future value")
    print("of a 10 year investment with")
    print("compounding interest and an additional")
    print("investment of a certain fixed amount each year.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the yearly interest rate: "))
    periods = eval(input("Enter the number of times interest is compounded each year: "))
    interest = rate / periods 
    yearlyinvestment = eval(input("Enter the fixed yearly amount to invest: "))
    
          
    for i in range(10):
          principal = principal + yearlyinvestment
          principal = principal * (1 + interest)

    print("The value in 10 years is:", principal, sep=" ")

main()

# alternative answer

# def main():
#     print("This program calculates the total future value")
#     print("of a multi-year investment with by describing")
#     print("the interest accrued in terms of a nominal rate")
#     print("and the number of compounding periods.")

#     principal = eval(input("Enter the initial principal: "))
#     interestrate = eval(input("Enter the interest rate: "))
#     periods = eval(input("Enter the number of compounding periods per year: "))
#     years = eval(input("Enter the number of years for the investment: "))

#     nominalrate = interestrate / periods
          
#     for i in range(periods * years):
#           principal = principal * (1 + nominalrate)

#     print("The value in ", years ,"years is:", principal, sep=" ")
