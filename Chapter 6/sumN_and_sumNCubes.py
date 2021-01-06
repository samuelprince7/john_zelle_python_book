# sum of N natural numbers and sum of cubes of the 1st N natural numbers
input_n = int(input("what is the number?: "))

def sumN(n):
    sum_n = 0
    for i in range(n+1):
        sum_n = sum_n + i 
    return sum_n 

def sumNCubes(n):
    sum_cubes_of_n = 0
    cube_of_i = 0
    for i in range(n+1):
        cube_of_i = i * i * i
        sum_cubes_of_n = sum_cubes_of_n + cube_of_i
    return sum_cubes_of_n

a = sumN(input_n)
b =sumNCubes(input_n)

print("The sum of the first {0} natural numbers is {1} , and the sum of the cubes of the first {0} natural \n numbers is {2}".format(input_n, a, b))
    