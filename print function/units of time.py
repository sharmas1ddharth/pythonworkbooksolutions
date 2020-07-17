seconds_in_day = 24*3600
seconds_in_hour = 3600
seconds_in_minutes = 60

days = int(input("Enter the number of days : "))
hour = int(input("Enter the number of hours : "))
minutes = int(input("Enter the number of minutes : "))
seconds = int(input("Enter the number of seconds : "))

total_seconds = seconds + (seconds_in_minutes * minutes) + (seconds_in_hour * hour) + (seconds_in_day * days)

print("Total seconds in ", days, "days", hour, "hours", minutes, "minutes", seconds, "seconds is = ", total_seconds)