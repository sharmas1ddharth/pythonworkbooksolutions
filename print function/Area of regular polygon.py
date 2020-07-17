import math

s = float(input("Enter the length of the sides : "))
n = int(input("Enter the number of sides : "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("Area of a regular polygon is : ", "{:.2f}".format(area))