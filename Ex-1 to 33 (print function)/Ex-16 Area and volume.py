import math

r = float(input("Enter the radius : "))

area_of_circle = math.pi*r**2
volume_of_sphere = (4/3) * math.pi * r ** 3

print("Area of circle is ", "{:.2f}".format(area_of_circle))
print("Volume of sphere is ", "{:.2f}".format(volume_of_sphere))