integer1 = int(input("Enter the first integer : "))
integer2 = int(input("Enter the second integer : "))
integer3 = int(input("Enter the third integer : "))

minimum = min(integer1, integer2, integer3)
maximum = max(integer1, integer2, integer3)
medium = integer1 + integer2 + integer3 - minimum - maximum

print("The sorted order is : ")
print(" ", minimum)
print(" ", medium)
print(" ", maximum)