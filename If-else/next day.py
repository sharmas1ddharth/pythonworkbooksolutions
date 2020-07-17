year = int(input("Enter the year : "))

if year % 400 == 0:
    leap_year = True

elif year % 100 == 0:
    leap_year = False

elif year % 4 == 0:
    leap_year = True

else:
    leap_year = False

month = int(input("Enter the month : "))

if month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28

elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    month_length = 31

else:
    month_length = 30

day = int(input("Enter the day here : "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
