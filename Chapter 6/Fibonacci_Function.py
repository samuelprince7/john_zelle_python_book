#'Fibonacci Calculator
# The program calculates the nth Fibonacci number.

number = int(input('What Fibonacci number in the sequence would you like to know?: '))

def fibonacci(n):
    n1 = 1
    n2 = 1
    for i in range(3, n+1):
        n1, n2 = n2, n1+n2
    return n2

example = fibonacci(number)

print()
print('The Fibonacci number', number, "is: ", example)
