# computes hourly wage based on input

hours = eval(input("How many hours did you work?: "))
rate = eval(input("What is your hourly wage?: "))

if hours > 40:
    print("You get overtime")
    base_pay = 40 * rate
    overtime_rate = rate * 1.5
    overtime_pay = (hours - 40) * overtime_rate
    wages = base_pay + overtime_pay
    
else: wages = hours * rate

print("Your total wages are:" , wages)