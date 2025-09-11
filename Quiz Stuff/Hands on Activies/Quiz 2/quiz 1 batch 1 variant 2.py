birthMonth = int(input('Enter your birth month [1-12]: '))
birthDay = int(input('Enter you birth day: '))
validityCheck = True

if birthMonth == 1 and (birthDay == 1 or birthDay < 20): 
    zodiac = 'Capricorn'
elif birthMonth == 1 and (birthDay == 20 or birthDay < 32):
    zodiac = 'Aquarius'
elif birthMonth == 2 and (birthDay == 1 or birthDay < 19):
    zodiac = 'Aquarius'
elif birthMonth == 2 and (birthDay == 19 or birthDay < 30):
    zodiac = 'Pisces'
elif birthMonth == 3 and (birthDay == 11 or birthDay < 20):
    zodiac = 'Pisces'
elif birthMonth == 3 and (birthDay == 21 or birthDay < 32):
    zodiac = 'Aries'
elif birthMonth == 4 and (birthDay == 1 or birthDay < 20):
    zodiac = 'Aries'
elif birthMonth == 4 and (birthDay == 20 or birthDay < 31):
    zodiac = 'Taurus'
elif birthMonth == 5 and (birthDay == 1 or birthDay < 20):
    zodiac = 'Taurus'
elif birthMonth == 5 and (birthDay == 21 or birthDay < 32):
    zodiac = 'Gemini'
elif birthMonth == 6 and (birthDay == 1 or birthDay < 21):
    zodiac = 'Gemini'
elif birthMonth == 6 and (birthDay == 21 or birthDay < 31):
    zodiac = 'Cancer'
elif birthMonth == 7 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Cancer'
elif birthMonth == 7 and (birthDay == 23 or birthDay < 32):
    zodiac = 'Leo'
elif birthMonth == 8 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Leo'
elif birthMonth == 8 and (birthDay == 23 or birthDay < 32):
    zodiac = 'Virgo'
elif birthMonth == 9 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Virgo'
elif birthMonth == 9 and (birthDay == 23 or birthDay < 31):
    zodiac = 'Libra'
elif birthMonth == 10 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Libra'
elif birthMonth == 10 and (birthDay == 23 or birthDay < 32):
    zodiac = 'Scorpio'
elif birthMonth == 11 and (birthDay == 1 or birthDay < 22):
    zodiac = 'Scorpio'
elif birthMonth == 11 and (birthDay == 22 or birthDay < 31):
    zodiac = 'Sagittarius'
elif birthMonth == 12 and (birthDay == 1 or birthDay < 22):
    zodiac = 'Sagittarius'
elif birthMonth == 12 and (birthDay == 22 or birthDay < 32):
    zodiac = 'Capricorn'
else:
    validityCheck = False

if validityCheck == True:
    print(f'Your zodiac sign is {zodiac}.')
else: 
    print('Wrong month or day.')