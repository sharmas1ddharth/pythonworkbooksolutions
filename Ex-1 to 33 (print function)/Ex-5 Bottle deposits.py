# Take input from user

less = float(input("Enter the number of bottle less than 1 litre : "))
more = float(input("Enter the number of bottle more than 1 litre : "))

# calculation

total = less * 0.10 + more * 0.25

# output line

print("Total refund is $", total)