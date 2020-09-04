pressure = float(input("Enter the pressure in kilo pascal : "))

pressure_in_pound_per_square_inch = pressure / 6.895
pressure_in_milimeter_mercury = pressure * 7.50
pressure_in_atmospheric_pressure = pressure * 0.00986923266

print("%0.2f pressure in kilo pascal is equals to %0.2f and  pressure in pound per square inch and %0.2f in millimeter mercury and %0.2f in atmospheric pressure"
      %(pressure, pressure_in_pound_per_square_inch, pressure_in_milimeter_mercury, pressure_in_atmospheric_pressure))