integer = int(input('Enter an integer: '))

if integer % 4 == 0:
    print('The number is divisible by 4.')
elif integer % 3 == 0:
    print('The number is divisible by 3.')
elif integer % 2 == 0:
    print('The number is divisible by 2.')
else:
    print('The number is not divisible by 2, 3, or 4.')