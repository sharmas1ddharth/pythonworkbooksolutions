number = int(input("Enter the integer : "))

x = number // 1000
x1 = (number - (x * 1000)) // 100
x2 = (number - (x * 1000) - (x1 * 100)) // 10
x3 = (number - (x * 1000) - (x1 * 100) - (x2 * 10))

print("The sum of digits of integer is :", x + x1 + x2 + x3)
