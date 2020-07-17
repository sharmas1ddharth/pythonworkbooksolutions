low = 0.0000000000001
x = int(input("Enter number here : "))
guess = x/2
good_enough = (guess * guess) - x

while abs(good_enough) > low:
    guess = (guess + (x / guess)) / 2
    good_enough = (guess * guess) - x

print(guess)
