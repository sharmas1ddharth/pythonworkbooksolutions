ab = int(input("Enter the first side of a triangle : "))
bc = int(input("Enter the second side of a triangle : "))
ca = int(input("Enter the third side of a triangle : "))


if ab == bc and bc == ca and ca == ab:
    print("This is an equilateral triangle ")

elif ab == bc  or ca == bc or ab == ca:
    print("This is an Isosceles Triangle")

else:
    print("This is an scalene triangle")