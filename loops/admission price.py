total_cost = 0

interrupted = True

while interrupted:
    age = (input('Enter age here : '))
    if age != '':
        age = int(age)
    else:
        break

    if age <= 2:
        cost = 0
    elif 3 <= age <= 12:
        cost = 14
    elif age >= 65:
        cost = 18
    elif 12 < age < 65:
        cost = 23
    else:
        break

    total_cost += cost

print('The total cost is %0.2f' % total_cost)
