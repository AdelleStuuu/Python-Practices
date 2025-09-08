birthMonth = int(input('Enter your birth month: '))
birthDay = int(input('Enter your birth day: '))

if (birthMonth == 12 and birthDay >= 22)  or (birthMonth == 1 and birthDay >= 19):
    print('Your zodiac sign is Capricorn.')
else:
    print('Your zodiac sign is not Capricorn.')