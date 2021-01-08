# this fuction makes an acronym of the phrase you type
# it is meant to illustrate the use of slicing strings and lists
# utilizing a for loop inside a function

def acronym(phrase):

    tphrase = phrase.title()

    Lphrase = tphrase.split()

    acronym_string = ""

    for wordstring in Lphrase:
        acronym_string = acronym_string + wordstring[0]

    return acronym_string

print(acronym("Samuel Levi Prince"))
print(acronym("Amy Rogers"))
print(acronym("Jeff Rogers"))
print(acronym("Colin Wong"))
print(acronym("Arthur Best"))
print(acronym("Hannah Ruth Marie Ade"))