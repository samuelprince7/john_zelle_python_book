# decision structure 1-5 for A-F 


def main():

    grade = int(input("Enter your number grade 0-5:"))

    if grade >= 5:
        print("Your grade is A")

    elif grade == 4:
        print("Your grade is B")

    elif grade == 3:
        print("Your grade is C")

    elif grade == 2:
        print("Your grade is D")

    elif grade == 1:
        print("Your grade is F")

    elif grade <= 0:
        print("Your grade is F")

main()

