birthMonth = int(input('Enter your birth month [1-12]: '))
birthDay = int(input('Enter you birth day: '))

if birthMonth == 1 and (birthDay == 1 or birthDay < 20): 
    zodiac = 'Capricorn'
    validityCheck = True 
elif birthMonth == 1 and (birthDay == 20 or birthDay < 32):
    zodiac = 'Aquarius'
    validityCheck = True 
elif birthMonth == 2 and (birthDay == 1 or birthDay < 19):
    zodiac = 'Aquarius'
    validityCheck = True 
elif birthMonth == 2 and (birthDay == 19 or birthDay < 30):
    zodiac = 'Pisces'
    validityCheck = True 
elif birthMonth == 3 and (birthDay == 11 or birthDay < 20):
    zodiac = 'Pisces'
    validityCheck = True 
elif birthMonth == 3 and (birthDay == 21 or birthDay < 32):
    zodiac = 'Aries'
    validityCheck = True 
elif birthMonth == 4 and (birthDay == 1 or birthDay < 20):
    zodiac = 'Aries'
    validityCheck = True 
elif birthMonth == 4 and (birthDay == 20 or birthDay < 31):
    zodiac = 'Taurus'
    validityCheck = True 
elif birthMonth == 5 and (birthDay == 1 or birthDay < 20):
    zodiac = 'Taurus'
    validityCheck = True 
elif birthMonth == 5 and (birthDay == 21 or birthDay < 32):
    zodiac = 'Gemini'
    validityCheck = True 
elif birthMonth == 6 and (birthDay == 1 or birthDay < 21):
    zodiac = 'Gemini'
    validityCheck = True 
elif birthMonth == 6 and (birthDay == 21 or birthDay < 31):
    zodiac = 'Cancer'
    validityCheck = True 
elif birthMonth == 7 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Cancer'
    validityCheck = True 
elif birthMonth == 7 and (birthDay == 23 or birthDay < 32):
    zodiac = 'Leo'
    validityCheck = True 
elif birthMonth == 8 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Leo'
    validityCheck = True 
elif birthMonth == 8 and (birthDay == 23 or birthDay < 32):
    zodiac = 'Virgo'
    validityCheck = True 
elif birthMonth == 9 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Virgo'
    validityCheck = True 
elif birthMonth == 9 and (birthDay == 23 or birthDay < 31):
    zodiac = 'Libra'
    validityCheck = True 
elif birthMonth == 10 and (birthDay == 1 or birthDay < 23):
    zodiac = 'Libra'
    validityCheck = True 
elif birthMonth == 10 and (birthDay == 23 or birthDay < 32):
    zodiac = 'Scorpio'
    validityCheck = True 
elif birthMonth == 11 and (birthDay == 1 or birthDay < 22):
    zodiac = 'Scorpio'
    validityCheck = True 
elif birthMonth == 11 and (birthDay == 22 or birthDay < 31):
    zodiac = 'Sagittarius'
    validityCheck = True 
elif birthMonth == 12 and (birthDay == 1 or birthDay < 22):
    zodiac = 'Sagittarius'
    validityCheck = True 
elif birthMonth == 12 and (birthDay == 22 or birthDay < 32):
    zodiac = 'Capricorn'
    validityCheck = True 
else:
    validityCheck = False

if validityCheck == True:
    print(f'Your zodiac sign is {zodiac}.')
else: 
    print('Wrong month or day.')