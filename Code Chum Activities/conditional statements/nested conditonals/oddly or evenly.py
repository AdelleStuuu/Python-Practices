number = int(input('Enter an integer: '))

if number % 2 != 0:
    if number % 3 == 0: 
        print('Oddly divisible by 3')
    else:
        print('Odd number')
else:
    if number % 4 == 0:
        print('Evenly divisible by 4')
    else:
        print('Even number')