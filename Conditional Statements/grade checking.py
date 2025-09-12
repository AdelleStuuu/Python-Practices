print()

while True:
    try:
        grade = int(input('Enter your raw grade here: '))
    except ValueError:
        print('Enter a valid integer.')
        continue

    if 100 >= grade >= 90:
        print('Your Grade equivalent is A')
        break
    elif 89 >= grade >= 80:
        print('Your Grade equivalent is B')
        break
    elif 79 >= grade >= 70:
        print('Your Grade equivalent is C')
        break
    elif 69 >= grade >= 60:
        print('Your Grade equivalent is D')
        break
    elif 59 >= grade >= 0:
        print('Your Grade equivalent is F')
        break
    else:
        print('Please input a valid grade number.')
        print()

print()