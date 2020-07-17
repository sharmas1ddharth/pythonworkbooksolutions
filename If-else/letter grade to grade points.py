letter_a_plus = 4.0
letter_a = 4.0
letter_a_minus = 3.7
letter_b_plus = 3.3
letter_b = 3.0
letter_b_minus = 2.7
letter_c_plus = 2.3
letter_c = 2.0
letter_c_minus = 1.7
letter_d_plus = 1.3
letter_d = 1.0
letter_f = 0

grade = input("Enter the grade you want to know the points of : ")

if grade == str.capitalize("a+"):
    print(letter_a_plus)

elif grade == str.capitalize("a"):
    print(letter_a)

elif grade == str.capitalize("a-"):
    print(letter_a_minus)

elif grade == str.capitalize("b+"):
    print(letter_b_plus)

elif grade == str.capitalize("b"):
    print(letter_b)

elif grade == str.capitalize("b-"):
    print(letter_b_minus)

elif grade == str.capitalize("c+"):
    print(letter_c_plus)

elif grade == str.capitalize("c"):
    print(letter_c)

elif grade == str.capitalize("c-"):
    print(letter_c_minus)

elif grade == str.capitalize("d+"):
    print(letter_d_plus)

elif grade == str.capitalize("d"):
    print(letter_d)

else:
    print(letter_f)

exit(0)