original_price = 0
new_price = 0

for item in range(5):
    original_price = (item * 5) + 4.95
    new_price = original_price * (60/100)

    print("The original price is {} and after 60% discount the new price is {}".format(original_price, new_price))