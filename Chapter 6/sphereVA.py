def sphere():
    print("This program finds the volume & surface area of a sphere based on its radius")
    print()

    r = float(input("Please enter the radius of your shpere: "))
    

    v = (4 * 3.14 * r**3)/3

    a = (4 * 3.14 * r**2)

    print()
    print("The volume of your sphere is:", v )
    print()
    print("The area of your sphere is:", a )

sphere()
    
