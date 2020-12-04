# zelle chp 5 exersise 8
# cearar cipher that shifts a word based on the key
# loops over zabc...

def main():

    message = input("what is the word to encode (or decode based a on negative key)? : ")

    key = int(input("How many places should it shift?: "))

    alphabet = ("0abcdefghijklmnopqrstuvwxyz")
    alphabet2 = ("abcdefghijklmnopqrstuvwxyz")
    alphabet3 = alphabet + (alphabet2 *7)

    encoded_message = ""

    for ch in message:
        num = alphabet3.find(ch) + key
        encoded_message = encoded_message + alphabet3[num]

    print(" The encoded message is:  {0}".format(encoded_message))

main()
