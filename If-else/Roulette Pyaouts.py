import random

value = random.randrange(0, 38)

if value == 37:
    print("The spin resulted in 00...")

elif value == 0:
    print("The spin resulted in 0...")

else:
    print("The spin resulted in %d..." % value)

# second condition

if value == 37:
    print("Pay", value)

else:
    print("Pay", value)

# third

if value == 0 or 00:
    print("Pay Green")

elif value == 1 and 3 and 5 and 7 and 9 and 12 and 14 and 16 and 18 and 19 and 21 and 23 and 25 and 27 and 30 and 32 and 34 and 36:
    print("Pay Red")

else:
    print("Pay Black")

# forth

if 1 <= value <= 36:
    if value % 2 == 1:
        print("Pay Odd")
    else:
        print("Pay even")

# fifth

if  1 <= value <= 18:
    print("Pay 1 to 18")

elif 19 <= value <= 36:
    print("Pay 19 to 36")
