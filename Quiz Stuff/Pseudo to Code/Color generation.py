print()
color = str(input('Enter a starting letter of a color: '))

print('Output 1')
if color == 'B' or color == 'b':
    print('The color is Blue')
elif color == 'R' or color == 'r':
    print('The color is Red')
elif color == 'Y' or color == 'y':
    print('The color is Yellow')
elif color == 'O' or color == 'o':
    print('The color is Orange')
elif color == 'W' or color == 'w':
    print('The color is White')
elif color == 'G' or color == 'g':
    print('The color is Green')
elif color == 'V' or color == 'v':
    print('The color is Violet')
else:
    print('Error, this is not a valid input')

print()
print('Output 2')

match color.upper():
    case ('B'):
        print('The color is Blue')
    case ('R'):
        print('The color is Red')
    case ('Y'):
        print('The color is Yellow')
    case ('O'):
        print('The color is Orange')
    case ('W'):
        print('The color is White')
    case ('G'):
        print('The color is Green')
    case ('V'):
        print('The color is Violet')
    case (_):
        print('input is invalid')
print()