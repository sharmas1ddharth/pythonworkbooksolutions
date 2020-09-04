inch_per_foot = 12
yard_per_foot = 0.333333
miles_per_foot = 0.000189394

measurement = int(input("Enter your measurement in feet : "))

distance_in_inch = measurement * inch_per_foot
distance_in_yards = measurement * yard_per_foot
distance_in_miles = measurement * miles_per_foot

print(measurement, "feet in inch is ", distance_in_inch)
print(measurement, "feet in yard is ", "{:.2f}".format(distance_in_yards))
print(measurement, "feet in miles is ", "{:.2f}".format(distance_in_miles))
