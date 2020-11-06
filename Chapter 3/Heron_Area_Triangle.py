import math

def heron():
    print("The program determines the area of a Triangle")
    print("based on Heron's formula")
    print("given the user inputs the length of each side")
    print("seperately")

    print()

    a = float(input("Enter the length of the 1st side: "))
    b = float(input("Enter the length of the 2nd side: "))
    c = float(input("Enter the length of the 3rd side: "))

    s = (a + b + c) / 2

    area = math.sqrt(s *(s-a) *(s-b) *(s-c))

    print()

    print("The Area of the Triangle is:", area )

heron()
