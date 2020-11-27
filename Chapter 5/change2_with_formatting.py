# change2_with_formatting.py
# A program to calculate the value of some change in dollars
# This version represents the total cash in cents.
# and makes use of the formating methods for dollars and cents

def main():
    print("Change Counter\n")
    print("Please enter the count of each coint type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("The total value of your change is ${0}.{1:0>2}"
            .format(total//100, total%100))

main()