#zelle chp 6 exersise 14

# reads the contents of a file that should be a list of string digits (multiple lines) in .txt format
# uses toNumbers to convert the string digits to numbers
# uses squareEach to square each number and return that value back into the list
# uses sumList to add the total of all the recently squared numbers

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    return strList

def squareEach(nums_list):
    for i in range(len(nums_list)):
        nums_list[i] = nums_list[i] ** 2
    return nums_list 

def sumList(nums_list):
    total = 0
    for i in range(len(nums_list)):
        total = nums_list[i] + total
    return total

someFile = input("what is the file name?:")

input_file = open(someFile, "r")

lines = input_file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split()
    toNumbers(lines[i])
    squareEach(lines[i])
    print(sumList(lines[i]))

input_file.close()

