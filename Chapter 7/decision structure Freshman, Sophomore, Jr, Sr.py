# decision structure Freshman, Sophomore, Junior, Senior

def main():

    credits = int(input("How many credits do you have?:"))

    if credits < 7:
        title = "Freshman" 

    elif credits >= 7 and credits <=15:
        title = "Sophomore" 

    elif credits >= 16 and credits <=25:
        title = "Junior" 

    else:
        title = 'Senior'

    print("Your title is", title)

if __name__ == '__main__':
    main()