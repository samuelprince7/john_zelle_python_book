# This program determines a grade
# Pulled from a List
# based on user input

def main():

    n = int(input("Enter your Quiz score between 1-5: "))
    
    Scores = ["F", "F", "D", "C", "B", "A"]

    Grade = Scores[n]

    print("Your Grade is:", Grade)

main()
