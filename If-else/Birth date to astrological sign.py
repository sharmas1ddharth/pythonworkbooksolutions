month = input("Enter month of your date of birth : ")
day = int(input('Enter day of date of birth : '))

if month == "january":
    if day < 20:
        sign = "Capricorn"
    else:
        sign = "Aquaris"

elif month == "february":
    if day < 19:
        sign = "Aquaris"
    else:
        sign = "Pisces"

elif month == "march":
    if day < 21:
        sign = "Pisces"
    else:
        sign = "Aries"

elif month == "april":
    if day < 20:
        sign = "Aries"
    else:
        sign = "Taurus"

elif month == "may":
    if day < 21:
        sign = "Taurus"
    else:
        sign = "Gemini"

elif month == "june":
    if day < 21:
        sign = "Gemini"
    else:
        sign = "Cancer"

elif month == "july":
    if day < 23:
        sign = "Cancer"
    else:
        sign = "Leo"

elif month == "august":
    if day < 23:
        sign = "Leo"
    else:
        sign = "Virgo"

elif month == "september":
    if day < 23:
        sign = "Virgo"
    else:
        sign = "Libra"

elif month == "october":
    if day < 23:
        sign = "Libra"
    else:
        sign = "Scorpio"

elif month == "november":
    if day < 22:
        sign = "Scorpio"
    else:
        sign = "Sagittarius"

elif month == "december":
    if day < 22:
        sign = "Sagittarius"
    else:
        sign = "Capricorn"

print("Your astrological sign is ", sign)







