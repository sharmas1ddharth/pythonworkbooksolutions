cents = int(input("Enter the money in cents you give : "))

cents_per_loonie = 100
cents_per_toonie = 200
cents_per_penny = 1
cents_per_dime = 10
cents_per_nickle = 5
cents_per_quarter = 25

print(" ", cents // cents_per_penny, "pennies")
print(" ", cents // cents_per_nickle, "nickles")
print(" ", cents // cents_per_dime, "dimes")
print(" ", cents // cents_per_quarter, "quarters")
print(" ", cents // cents_per_loonie, "loonies")
print(" ", cents // cents_per_toonie, "toonies")