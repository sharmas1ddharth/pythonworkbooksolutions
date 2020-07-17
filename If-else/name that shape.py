shape = {"3": "triangle",
         "4": "rectangle",
         "5": "pentagon",
         "6": "hexagon",
         "7": "heptagon",
         "8": "octagon",
         "9": "nonagon",
         "10": "decagon", }

sides = input("Enter the number of sides : ")

if sides in shape:
    print(shape[sides])

else:
    print("Error : enter correct value")
