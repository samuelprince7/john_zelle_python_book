# this is the infamous Syracuse sequence  (which is still an open debate amoungst math maticians) 
# in a function, that also prints each number in the sequence
# seems to be true but, maybe in can be proved wrong

#by starting w/a natural number , applying this sequence,
# should always eventually resutl in 1

#syr(x) = x/2  if x is even
#       = 3x +1  if x iss odd

#define the function

def syr(number):
    if number % 2 != 0: #this line says "if x is odd"
        number2 = (3 * number) + 1
    else:
        number2 = number/2
    return number2

def main():
    
    x = int(input("Please enter a whole number"))

    while x !=1:
        x = syr(x)
        print(x)

main()

