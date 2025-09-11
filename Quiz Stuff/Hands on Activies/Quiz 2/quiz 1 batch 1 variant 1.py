birthMonth = int(input('Enter your birth month [1-12]: '))
birthDay = int(input('Enter you birth day: '))

if birthMonth == 1 and (birthDay == 1 or birthDay < 20): 
    z = 'Capricorn'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 1 and (birthDay == 20 or birthDay < 32):
    z = 'Aquarius'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 2 and (birthDay == 1 or birthDay < 19):
    z = 'Aquarius'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 2 and (birthDay == 19 or birthDay < 30):
    z = 'Pisces'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 3 and (birthDay == 11 or birthDay < 20):
    z = 'Pisces'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 3 and (birthDay == 21 or birthDay < 32):
    z = 'Aries'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 4 and (birthDay == 1 or birthDay < 20):
    z = 'Aries'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 4 and (birthDay == 20 or birthDay < 31):
    z = 'Taurus'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 5 and (birthDay == 1 or birthDay < 20):
    z = 'Taurus'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 5 and (birthDay == 21 or birthDay < 32):
    z = 'Gemini'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 6 and (birthDay == 1 or birthDay < 21):
    z = 'Gemini'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 6 and (birthDay == 21 or birthDay < 31):
    z = 'Cancer'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 7 and (birthDay == 1 or birthDay < 23):
    z = 'Cancer'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 7 and (birthDay == 23 or birthDay < 32):
    z = 'Leo'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 8 and (birthDay == 1 or birthDay < 23):
    z = 'Leo'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 8 and (birthDay == 23 or birthDay < 32):
    z = 'Virgo'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 9 and (birthDay == 1 or birthDay < 23):
    z = 'Virgo'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 9 and (birthDay == 23 or birthDay < 31):
    z = 'Libra'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 10 and (birthDay == 1 or birthDay < 23):
    z = 'Libra'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 10 and (birthDay == 23 or birthDay < 32):
    z = 'Scorpio'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 11 and (birthDay == 1 or birthDay < 22):
    z = 'Scorpio'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 11 and (birthDay == 22 or birthDay < 31):
    z = 'Sagittarius'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 12 and (birthDay == 1 or birthDay < 22):
    z = 'Sagittarius'
    print(f'Your zodiac sign is {z}.')
elif birthMonth == 12 and (birthDay == 22 or birthDay < 32):
    z = 'Capricorn'
    print(f'Your zodiac sign is {z}.')
else: 
    print('Wrong month or day.')