# program that determines the numeric value of a name
# mainly shows how to convert letters to values

def main():

    name = input('What is your first OR last name?: ')

    alphabet = ("0abcdefghijklmnopqrstuvwxyz")

    name1 = name.lower()

    numeric_value = 0

    for ch in name1:
        numeric_value = numeric_value + alphabet.find(ch)
        # this could also be written as numeric_value += alphabet.find(ch)

    print("The value of your name is {0}".format(numeric_value))

main()

