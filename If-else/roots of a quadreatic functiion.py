import math

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))

root = b**2 - 4*a*c

if root > 0:
    num_root = 2
    x1 = ((-b) + (math.sqrt(root)) / (2*a))
    x2 = -b - (math.sqrt(root)) / (2*a)
    print("There are two roots %f and %f" %(x1, x2))

elif root == 0:
    num_root = 1
    x = (-b) / 2*a
    print("There is only one root %f" %(x))

else:
    print("There are no roots")

exit("bye")