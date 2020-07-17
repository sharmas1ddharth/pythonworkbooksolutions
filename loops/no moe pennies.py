actualsum = 0
roundedsum = 0

interrupted = False
while not interrupted:
    price = input("Enter a price : ")

    if price != "":
        price =float(price)
    else:
        break

    actualsum += price
    price_in_pennies = price * 100
    remainder = price_in_pennies % 5

    if remainder > 2.5:
        price_in_pennies += 5-remainder
    else:
        price_in_pennies -= remainder

    roundedprice = price_in_pennies * 0.01
    roundedsum += roundedprice

print("The actual sum is {}".format(round(actualsum, 2)))
print("The rounded sum paid with cash is {}".format(round(roundedsum, 2)))