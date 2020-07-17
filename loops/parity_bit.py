bit = input("Enter bit here : ")
print(" ")
while bit != "":

    if len(bit) != 8:
        print("Error enter 8 bits")

    else:
        number_of_ones = bit.count("1")
        if number_of_ones % 2 == 0:
            print("Parity bit is 0")
            print(" ")
        else:
            print("Parity bit is 1")
            print(" ")
    bit = input("Enter bit here : ")
