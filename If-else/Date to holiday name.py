

month = int(input("Enter the month you want to check for : "))
day = int(input("Enter the day you want to check for : "))

if month == 1 and day == 1:
    print("Today is New Year's Day")

elif month == 7 and day == 1:
    print("Today is Canada Day")

elif month == 12 and day == 25:
    print("Today is Christmas_day")

else:
    print("Entered month and day do not correspond to a fixed-date holiday")