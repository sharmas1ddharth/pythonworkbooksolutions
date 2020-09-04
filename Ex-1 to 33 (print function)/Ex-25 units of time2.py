seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input("Enter the number of seconds : "))

days = seconds / seconds_in_day
seconds = seconds % seconds_in_day

hour = seconds / seconds_in_hour
seconds = seconds % seconds_in_hour

minutes = seconds / seconds_in_minute
seconds = seconds % seconds_in_minute

seconds = seconds


print("Time is ", "%02d: %02d: %02d: %02d" % (days, hour, minutes, seconds))
