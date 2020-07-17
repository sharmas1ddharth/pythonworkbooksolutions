rating = float(input("Enter the rating to know your performance and amount : "))

performance = [0]

if rating == 0.0:
    performance = "Unacceptable performance"
    amount_raise = 0.0 * 2400.00

elif rating == 0.4:
    performance = "Acceptable performance"
    amount_raise = 0.4 * 2400.00

elif rating == 0.6:
    performance = "Meritorious performance"
    amount_raise = 0.6 * 2400.00

elif rating > 0.6:
    performance = "Meritorious performance"
    amount_raise = rating * 2400.00

else:
    print("Enter correct rating")

print("Your performance is", performance, "and your amount raise is", amount_raise)
