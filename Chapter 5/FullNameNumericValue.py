# program that determines the numeric value of a name
# mainly shows how to convert letters to values

def main():

    name = input('What is your first, middle, and last name?: ')

    first, middle, last = name.split()

    alphabet = ("0abcdefghijklmnopqrstuvwxyz")

    name1 = first.lower()
    name2 = middle.lower()
    name3 = last.lower()

    numeric_value1 = 0
    numeric_value2 = 0
    numeric_value3 = 0

    for ch in name1:
        numeric_value1 = numeric_value1 + alphabet.find(ch)
        # this could also be written as numeric_value += alphabet.find(ch)

    for ch in name2:
        numeric_value2 = numeric_value2 + alphabet.find(ch)

    for ch in name3:
        numeric_value3 = numeric_value3 + alphabet.find(ch)

    final_value = numeric_value1 + numeric_value2 + numeric_value3

    print("The value of your name is {0}".format(final_value))

main()