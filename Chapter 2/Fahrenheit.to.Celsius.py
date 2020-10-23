def main():
    for i in range(5):
        fahrenheit = eval(input("What is the fahrenheit temperature? "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The temperature is", celsius, "degrees Celsius.")


main()
