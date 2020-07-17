temperature_in_celsius = 0
temperature_in_fahrenheit = 0

for temperature_in_celsius in range(0, 101, 10):
    if temperature_in_celsius <= 100 and temperature_in_celsius % 10 == 0:
        temperature_in_fahrenheit = (temperature_in_celsius * (9/5)) + 32
        print("%d degree in celsius  = %d degree in fahrenheit " %(temperature_in_celsius, temperature_in_fahrenheit))
