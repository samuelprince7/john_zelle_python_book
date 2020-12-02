# cearar cipher that shifts a word based on the key

def main():

    message = input("what is the word to encode (or decode based a on negative key)? : ")

    key = int(input("How many places should it shift?: "))

    encoded_message = ""

    for ch in message:
        num = int(ord(ch))
        num2 = num + key
        letter = chr(num2)
        encoded_message = encoded_message + letter 

    print(" The encoded message is {0}".format(encoded_message))

main()


