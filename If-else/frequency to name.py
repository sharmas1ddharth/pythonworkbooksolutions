frequency_range = float(input("Enter the frequency range : "))

if frequency_range < 3 * 10**9:
    name = "Radio waves"

elif 3 * 10**9 < frequency_range < 3 * 10**12:
    name = "Microwaves"

elif 3 * 10**12 < frequency_range < 4.3 * 10 **14:
    name = "Infrared lights"

elif 4.3 * 10**14 < frequency_range < 7.5 * 10**14:
    name = "Visible light"

elif 7.5 * 10**14 < frequency_range < 3 * 10**17:
    name = "Ulraviolet light"

elif 3 * 10**17 < frequency_range < 3 * 10**19:
    name = "X - rays"

elif 3 * 10**19 < frequency_range:
    name = "Gamma rays"

else:
    print("Enter correct value")

print(name)