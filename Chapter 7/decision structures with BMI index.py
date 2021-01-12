# decision structures with BMI index

weight = int(input("What is your weight in pounds?"))

height = int(input("What is your height in inches?"))

height_sq = height **2

weight_x_720 = weight * 720

BMI = weight_x_720 / height_sq 

if BMI >=19 and BMI <=25:
    print("Your BMI is within the healthy range")

elif BMI <=18:
    print("Your BMI is BELOW the healthy range")

elif BMI >=26:
    print("Dude your BMI is ABOVE the healthy range")

else:
    print("Something went wrong. The BMI healthy range is between 19-25")

print("Your BMI is : " , BMI)