def fibonacci():
    print('Fibonacci Calculator')
    print('The program calculates the nth Fibonacci number.')

    n = int(input('What Fibonacci number in the sequence would you like to know?: '))

    n1 = 1
    n2 = 1

    for i in range(3, n+1):
        n1, n2 = n2, n1+n2


    print()
    print('The Fibonacci number F(', n, ') is ', n2, '.', sep='')

fibonacci()

    
