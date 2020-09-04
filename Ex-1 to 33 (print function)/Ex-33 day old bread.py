fresh_bread = 3.49

number_of_day_old_bread = int(input("Enter the number of day old bread : "))

day_old_bread_price = 3.49 * (60/100)

total_price_of_day_old_bread = number_of_day_old_bread * day_old_bread_price

print("All the prices of bread is listed below :")
print("Price of regular bread : $", fresh_bread)
print("Price of day old bread : $", "{:.2f}".format(day_old_bread_price))
print("Price of %0.2d  day old bread is $ %0.2d" %(number_of_day_old_bread, total_price_of_day_old_bread))