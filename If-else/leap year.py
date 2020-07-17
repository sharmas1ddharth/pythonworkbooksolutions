year = int(input("Enter the year :"))

leapyear = [0]

if year % 400 == 0:
    leapyear = True

elif year % 100 == 0:
    leapyear = False

elif year % 4 == 0:
    leapyear = True

else:
    leapyear = False

if leapyear == True:
    print(year, "is a leap year")

else:
    print(year, "is not a leap year")