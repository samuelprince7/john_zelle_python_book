# This program determines the area of a Triangle
# based on Heron's formula
# given the user inputs the length of each side
# seperately

input_a = float(input("Enter the length of the 1st side: "))
input_b = float(input("Enter the length of the 2nd side: "))
input_c = float(input("Enter the length of the 3rd side: "))

def heron_tri_area(a, b, c):
    import math 
    s = (a + b + c) / 2
    area = math.sqrt(s *(s-a) *(s-b) *(s-c))
    return area

specific_triangles_area = heron_tri_area(input_a, input_b, input_c)

print("The Area of the Triangle is {0:0.3f} . ".format(specific_triangles_area)) 
