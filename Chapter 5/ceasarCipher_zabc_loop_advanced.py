#this program creates a ceasar cipher based on the a-z alphabet
# and loops through itself xyz...abc
# accomodates for lowercase and capital letters
# and includes a section that can function as a dycryter 

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    abcs = alphabet * 2 + alphabet.upper()*2

    # get string from user
    user_string = input("Enter the text you'd like to encode: ")

    # get the key for encoding 
    key = int(input('Enter an integer between 1 and 25 to act as the key value for encryption: '))

    # Encode the message
    encoded_message = ""
    for word in user_string.split():
        for character in word:
            # what is inside [abcs.find(character) + key] is a an actual number, or numeric value
            # then we are indexing abcs by that number, so abcs[8] is i, abcs[2] is c, abcs[0] is a
            # and abcs[25] is z, abcs[26] is a, abcs[52] is A, 
            # using abcs.find and adding the key eliminates the needs for any complex math solving
            encoded_message = encoded_message + abcs[abcs.find(character) + key]
        #now we add a space after each word 
        encoded_message = encoded_message + ' '

    #now we slice, in order to stip off the last space
    encoded_message = encoded_message[:-1] 

    print('\nYour encrypted  message reads:')
    print(encoded_message)

    #this section of the code decodes the message back to the user

    decoded_message = ""
    for word in encoded_message.split():
        for ch in word:
            # we add 26 to the letter in order to get the same letter 
            # in the 2nd abc sequence , example a[0] +26 is 26, b[1]+26 is 27, c[2]+26 is 28
            # so we can then subtract the key adequately 
            # the addition of the 26 is the hardest part of the code to discern, but it works very well
            decoded_message += abcs[abcs.find(ch) + 26 - key]
        # again we add a space after each full word
        decoded_message += " " 
    
    #now we strip off the last piece of white space
    decoded_message = decoded_message[:-1]

    print('\nYour original message should read exactly below')
    print(decoded_message) 

main()

    


