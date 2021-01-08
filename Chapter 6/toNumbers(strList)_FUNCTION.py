# a function that returns a list of strings as a number

def toNumbers(strList):
    count = 0
    for i in range(len(strList)):
        count = count + 1
        strList[i] = count
    return strList

print(toNumbers(["number one", "number two", "number three"]))
print(toNumbers(["5", "2", "3"]))
print(toNumbers(["5", "10", "20", "40"]))