color = input('Enter a letter: ')

match color:
    case 'r':
        print('Red')
    case 'o':
        print('Orange')
    case 'y':
        print('Yellow')
    case 'g':
        print('Green')
    case 'b':
        print('Blue')
    case 'i':
        print('Indigo')
    case 'v':
        print('Violet')
    case _:
        print('Error')