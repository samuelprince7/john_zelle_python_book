# decision structure age limit for senate & house

age = int(input("what is your age?"))

years_a_cit = int(input("how many years have you been a US citizen?"))

if age >= 30 and years_a_cit >=9:
    print("You ARE eligible to be a US Senator")

else:   
    print("You are NOT eligible to be a Senator")

if age >=25 and years_a_cit >=7:
    print("You ARE eligible to be a House member")

else:
    print("You are NOT eligible to be a House member")

