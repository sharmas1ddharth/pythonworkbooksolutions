from math import log10

a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))

print("Sum of a and b is ", a+b)
print("Difference when b is subtracted from a is ", b-a)
print("Product of a and b is ", a*b)
print("Quotient when a is divided by b is ", a / b)
print("Remainder when a is divided by b is ", a % b)
print("Result of log(10(a)) is ", log10(a))
print("Result of b power of a is ", a**b)