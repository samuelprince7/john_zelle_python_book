# displays area & volume of a sphere based on radius input

r_input = float(input("Please enter the radius of your shpere: "))

def sphereArea(radius):
    area = (4 * 3.14 * radius**2)
    return area

def sphereVolume(radius):
    volume = (4 * 3.14 * radius**3)/3
    return volume
    

a = sphereArea(r_input)
v = sphereVolume(r_input)

  #  v = (4 * 3.14 * r**3)/3

  #  a = (4 * 3.14 * r**2)

print()
print("The volume of your sphere is {0:0.2f} and the area is {1:0.2f}".format(v,a) )
    

