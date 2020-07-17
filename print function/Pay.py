hours = float(input("Hours you work : "))
rate = float(input("Pay rate : "))

if hours > 40:
    pay = (40 * rate) + (rate * 1.5) * (hours - 40)

    print('Pay', pay)

else:
    pay = hours * rate
    print("pay", pay)
