month = input("Enter the name of the month : ")
day = int(input("Enter the day of the month : "))

if month in ("january", "february", "march"):
    season = "winter"

elif month in ("april", "may", "june"):
    season = "spring"

elif month in ("july", "august", "september"):
    season = "summer"

elif month in ("october", "november", "december"):
    season = "fall"

if month == "march" and day < 20:
    season = "winter"

elif month == "june" and day < 21:
    season = "spring"

elif month == "september" and day < 22:
    season = "summer"

elif month == "december" and day < 21:
    season = "fall"

print(season)