print()
while True:
    try:
        number = int(input('Enter any number: '))
    except ValueError:
        print('Enter an integer value.')
        print()
        continue
    
    break

if number > 0:
    print('The number is a positive number.')
elif number < 0:
    print('The number is a negative number.')
else:
    print('The number is zero.')
print()