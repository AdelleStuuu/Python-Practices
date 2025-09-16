
while True:
    print()
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('Enter an Integer.')
        
        continue
    else:
        if 20 >= number >= 10:
            print('The number is within range! Good job!')
            break
        else:
            print('Oop, Try again!')
print()

