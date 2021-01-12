# decision structure grade 0 to 100 

def main():

    score = int(input("Enter your number score between 0 and 100:"))

    if score >= 90:
        grade = "A" 

    elif score >= 80 and score <=89:
        grade = "B" 

    elif score >= 70 and score <=79 :
        grade = "C"     

    elif score >= 60 and score <=69:
        grade = "D" 

    elif score >= 50 and score <=59:
        grade = 'F'

    else:
        grade = 'F'

    print("Your grade is", grade)

if __name__ == '__main__':
    main()
