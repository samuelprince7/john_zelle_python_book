# decision structure speed limit & fine
# zelle chpt 7, #6

speed_limit = int(input("What is the speed limit?"))

clocked_speed = int(input("What was the clocked speed?"))

if clocked_speed <= speed_limit:
    print("Your speed is legal")

if clocked_speed > speed_limit:
    print("You are speeding")
    amount_over = clocked_speed - speed_limit
    amount_over_x5 = amount_over * 5
    total = amount_over_x5 + 50

if clocked_speed > 90:
    total = total + 200

if clocked_speed > speed_limit:
    print("Your total fine is:", total)