# word counter

def main():

    SomeFile = input("What file are we counting?: ")

    readFile = open(SomeFile, 'r')

    line_count = 0
    word_count = 0
    letter_count = 0

    for line in readFile:
        line_count = line_count + 1
        for word in line.split():
            word_count = word_count + 1
            for letter in word:
                letter_count = letter_count + 1

    print("There are {0} lines, {1} word, and {2} letters in that file".format(line_count, word_count, letter_count))

main()

