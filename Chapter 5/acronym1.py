# this program makes an acronym of the phrase you type
# it is meant to illustrate the use of slicing strings and lists
# inside a for loop

def main():

    phrase = str(input("Enter a phrase of words seperated by a space: "))

    tphrase = phrase.title()

    Lphrase = tphrase.split()

    acronym = ""

    for wordstring in Lphrase:
        acronym = acronym + wordstring[0]

    print("The acronym of the phrase is: ", acronym)

main()

