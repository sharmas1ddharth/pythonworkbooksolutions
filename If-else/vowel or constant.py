import random
alphabet = input("Enter the alphabet here : ")
vowel = {"a", "e", "i", "o", "u"}

if alphabet in vowel:
    print("%c is a vowel" % (alphabet))

elif alphabet == "y":
    print("Sometimes 'y' is a vowel and sometimes 'y' is a constant")

else:
    print("%c is a constant" % (alphabet))
