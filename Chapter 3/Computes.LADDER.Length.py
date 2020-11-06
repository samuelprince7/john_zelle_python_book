import math

def ladderlength():
    print("This program finds how long your ladder needs to be")
    print("in order to reach a given height")
    print("but you need to input the given height you need to reach")
    print("and the angle at the bottom of the ladder, in degrees.")

    height = float(input("How high is the point that you need to reach?: "))
    angle_degrees = float(input("what is the angle in degrees, at the bottom of the ladder?: "))

    angle_radians = (math.pi / 180) *angle_degrees

    ladder_Length = height / (math.sin(angle_radians))

    print()
    print("The length that your ladder needs to be to reach:", height )
    print("IS:", ladder_Length )

ladderlength()
