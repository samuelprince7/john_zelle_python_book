def grade(score):
    for i in range (10):

        #Use the append method to assign variables to values
        grade_list = []
        for x in range(0, 60):
            grade_list.append("F")
        for x in range(60, 70):
            grade_list.append("D")
        for x in range(70, 80):
            grade_list.append("C")
        for x in range(80, 90):
            grade_list.append("B")
        for x in range(90, 110):
            grade_list.append("A")

        #pass number grade into function as score parameter

        #return results in function grade
        return grade_list[score]

print(grade(59))
print(grade(60))
print(grade(70))
print(grade(80))
print(grade(90))
print(grade(100))