T = float(input("Enter the air temperature : "))
V = float(input("Enter the wind speed : "))

WCI = 13.12 + (0.6215*T) - (11.37 * V ** 0.16) + (0.3965 * T * V**0.16)

print("Wind chill index is", "{:.2f}".format(WCI))