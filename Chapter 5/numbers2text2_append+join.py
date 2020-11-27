# numbers2text2_append+join
# A program to convert sequence of Unicode numbers into
# a string of text. Efficient version using a list accumulator.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    #Get the message to encode
    inString = input("Enter the sequence of Unicode numbers: ")

    # Loop through each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr) #converts digits to a number
        chars.append(chr(codeNum))  #accumulate new character to the list chars via append

    message = "".join(chars)
    print("\nThe decoded message is:", message)

main()