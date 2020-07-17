points = float(input("Enter the points you want to know the grades of : "))

grade = [0]

if points >= 4.0:
    grade = "A+"

elif 4.0 == points:
    grade = "A"

elif 3.7 < points < 4.0:
    grade = "A-"

elif 3.3 < points < 3.7:
    grade = "B+"

elif 3.0 < points < 3.3:
    grade = "B"

elif 2.7 < points < 3.0:
    grade = "B-"

elif 2.3 < points < 2.7:
    grade = "C+"

elif 2.0 < points < 2.3:
    grade = "C"

elif 1.7 < points < 2.0:
    grade = "C-"

elif 1.3 < points < 1.7:
    grade = "D+"

elif 1.0 < points < 1.3:
    grade = "D"

elif 0 <= points < 1.0:
    grade = "F"

else:
    print("Enter correct value")

print("Grade is ", grade)

exit("Bye bye")