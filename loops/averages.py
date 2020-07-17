sums = 0
n = 0

interrupted = False

while not interrupted:
    val = int(input("Enter a value (0 to exit) : "))
    if val != 0:
        sums += val
        n += 1
    else:
        interrupted = True

average = sums / n
print("The average is {}".format(average))