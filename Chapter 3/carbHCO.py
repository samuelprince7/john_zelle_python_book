def carb():
    print("This program computes the molecular weight")
    print("of a carbohydrate based on")
    print("the number of hydrogen, carbon, and oxygen atoms in the molecule.")

    h = int(input("Please enter the number of hydrogen atoms: "))

    c = int(input("Please enter the number of carbon atoms: "))

    o = int(input("Please enter the number of oxygen atoms: "))

    weight = (h*1.00794) + (c*12.0107) + (o*15.9994)

    print()
    print("The molecular weight of your carboydrate")
    print("in grams per mole is:", weight )

carb() 
