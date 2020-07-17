import math

s1 = int(input("Enter the first side of triangle : "))
s2 = int(input("Enter the second side of triangle : "))
s3 = int(input("Enter the third side of triangle : "))

s = (s1 + s2 + s3) / 2

area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("Area of triangle with sides", "s1 =", s1, "s2 =", s2, "s3 =", s3, "is", area)