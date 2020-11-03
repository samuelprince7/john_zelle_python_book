def main():
    print("This program calculates the number of days between Jan 1")
    print("and the previous new moon")
    print("which number is used to determine easter")

    year = int(input("Enter the 4 digit year: "))
                
    c = year // 100
                
    epact = (8 + c//4 - c + (8*c +13)//25 + 11*(year%19))%30
                

    print("The number of days between January 1st and the previous new moon is:")
    print(epact)

main()

            


    
