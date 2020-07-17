days_in_month = {"january": "31",
                 "february": "28 or 29",
                 "march": "31",
                 "april": "30",
                 "may": "31",
                 "june": '30',
                 "july": "31",
                 "august": "31",
                 "september": "30",
                 "october": "31",
                 "november": "30",
                 "december": "31", }

month = input("Enter the name of the month here : ")

if month in days_in_month:
    print("There are", days_in_month[month], "days")

else:
    print("Error : Enter valid name")