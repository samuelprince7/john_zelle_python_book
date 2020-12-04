# program that determines the numeric value of a full name
# mainly shows how to convert letters to values
# as well as double loop iteration 

def main():

    name0 = input('What is your full name?: ')

    namel = name0.lower()

    name_list = namel.split()

    alphabet = ("0abcdefghijklmnopqrstuvwxyz")

    numeric_value = 0


    for name_string in name_list:
        for character in name_string:
            numeric_value = numeric_value + alphabet.find(character)
            # this could also be written as numeric_value += alphabet.find(character)


    print("The value of your name is {0}".format(numeric_value))

main()
