year = int(input('Enter a year: '))

if year % 100 == 0: 
    if year % 400 == 0: 
        print('It\'s a leap century year.')
    else:
        print('It\'s a century year.')
elif year % 100 != 0:
    if year % 4 == 0:
        print('It\'s a leap year.')
    elif year % 400 != 0:
        print('It\'s neither a leap year nor a century year.')