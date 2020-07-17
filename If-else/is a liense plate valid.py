plate = input("Enter the license plate number : ")

if len(plate) == 6 and  "A" <= plate[0] <= "Z" and \
        "A" <= plate[1] <= "Z" and \
        "A" <= plate[2] <= "Z "and \
        "0" <= plate[3] <= "9" and \
        "0" <= plate[4] <= "9" and \
        "0" <= plate[5] <= "9":

    print("The plate is for older numbers")

elif len(plate) == 7 and  "A" <= plate[0] <= "Z" and \
        "A" <= plate[1] <= "Z" and \
        "A" <= plate[2] <= "Z "and \
        "0" <= plate[3] <= "9" and \
        "0" <= plate[4] <= "9" and \
        "0" <= plate[5] <= "9" and \
        "0" <= plate[6] <= "9":
    print("The plate is valid for 4 numbers")

else:
    print("Enter a valid plate number")

