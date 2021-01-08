# zelle chp 6 exersise 13
# holds the most utility and cleanest (self adapted code)

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    return strList
    

print(toNumbers(['2', '3.3', '-7']))