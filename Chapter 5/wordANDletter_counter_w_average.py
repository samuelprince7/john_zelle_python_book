# this program determines the number of letters & words in a sentence
# as well as the average word length

def main():
    print("This program finds the number ")
    print("of words and letters in a sentence")

    sentence = input("Please write the sentence: ")

    List = sentence.split()

    number_of_words = 0
    number_of_letters = 0

    for word in List:
        number_of_words = number_of_words + 1

    for word in List:
        for letter in word:
            number_of_letters = number_of_letters + 1

    average = number_of_letters / number_of_words

    print("There are {0} words and {1} letters in your sentence, and the average word length is {2} letters".format(number_of_words,number_of_letters, average))

main()                                   