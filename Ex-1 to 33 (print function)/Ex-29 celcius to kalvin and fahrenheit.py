from math import radians

temp_in_celsius = float(input("Enter the temperature in  celsius : "))

temp_in_fahrenheit = (temp_in_celsius * 9/5) + 32
temp_in_kelvin = temp_in_celsius + 273.15

print("%0.2f in celsius is : %0.2f in fahrenheit and %0.2f in kelvins" %(temp_in_celsius, temp_in_fahrenheit, temp_in_kelvin))