violet = range(380, 449)
blue = range(450, 494)
green = range(495, 569)
yellow = range(570, 589)
orange = range(590, 619)
red = range(620, 749)

wavelength = int(input("Enter the wavelength : "))

if wavelength in violet:
    print("The color is violet")

elif wavelength in blue:
    print("The color is blue")

elif wavelength in green:
    print("The color is green")

elif wavelength in yellow:
    print("The color is yellow")

elif wavelength in orange:
    print("The color is orange")

elif wavelength in red:
    print("The color is red")

else:
    print("Error")
