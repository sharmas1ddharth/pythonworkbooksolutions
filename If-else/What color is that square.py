
letter = input("Enter the column(or letter) : ")
number = int(input("Enter the row(or number) : "))

if letter == "a" and number == 1 or letter == "c" and number == 3 or letter == "e" and number == 5 or letter == "g" and number == 7:
    print("The chess block is black")

else:
    print("The chess block is white")

