import math

r = int(input("Enter the radius of the cylinder : "))
h = int(input("Enter the height of the cylinder : "))

volume_of_cylinder = 2 * math.pi * r * h

print("Volume of cylinder is ","{:.1f}".format(volume_of_cylinder))