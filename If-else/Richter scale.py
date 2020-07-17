magnitude = float(input("Enter the magnitude of earthquake : "))
description = [0]

if magnitude < 2.0:
    description = "Micro"

elif 2.0 < magnitude < 3.0:
    description = "Very minor"

elif 3.0 < magnitude < 4.0:
    description = "Minor"

elif 4.0 < magnitude < 5.0:
    description = "Light"

elif 5.0 < magnitude < 6.0:
    description = "Moderate"

elif 6.0 < magnitude < 7.0:
    description = "Strong"

elif 7.0 < magnitude < 8.0:
    description = "Major"

elif 8.0 < magnitude < 10.0:
    description = "Great"

else:
    description = "Meteoric"

print("The description of the earthquake of magnitude you provide is", description)
