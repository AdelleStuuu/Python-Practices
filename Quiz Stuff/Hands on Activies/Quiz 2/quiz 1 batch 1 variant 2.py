birthMonth = int(input('Enter your birth month [1-12]: '))
birthDay = int(input('Enter you birth day: '))

if birthMonth == 1 and (birthDay == 1 or birthDay < 20): 
    z = 'Capricorn'
    validityCheck = True 
elif birthMonth == 1 and (birthDay == 20 or birthDay < 32):
    z = 'Aquarius'
    validityCheck = True 
elif birthMonth == 2 and (birthDay == 1 or birthDay < 19):
    z = 'Aquarius'
    validityCheck = True 
elif birthMonth == 2 and (birthDay == 19 or birthDay < 30):
    z = 'Pisces'
    validityCheck = True 
elif birthMonth == 3 and (birthDay == 11 or birthDay < 20):
    z = 'Pisces'
    validityCheck = True 
elif birthMonth == 3 and (birthDay == 21 or birthDay < 32):
    z = 'Aries'
    validityCheck = True 
elif birthMonth == 4 and (birthDay == 1 or birthDay < 20):
    z = 'Aries'
    validityCheck = True 
elif birthMonth == 4 and (birthDay == 20 or birthDay < 31):
    z = 'Taurus'
    validityCheck = True 
elif birthMonth == 5 and (birthDay == 1 or birthDay < 20):
    z = 'Taurus'
    validityCheck = True 
elif birthMonth == 5 and (birthDay == 21 or birthDay < 32):
    z = 'Gemini'
    validityCheck = True 
elif birthMonth == 6 and (birthDay == 1 or birthDay < 21):
    z = 'Gemini'
    validityCheck = True 
elif birthMonth == 6 and (birthDay == 21 or birthDay < 31):
    z = 'Cancer'
    validityCheck = True 
elif birthMonth == 7 and (birthDay == 1 or birthDay < 23):
    z = 'Cancer'
    validityCheck = True 
elif birthMonth == 7 and (birthDay == 23 or birthDay < 32):
    z = 'Leo'
    validityCheck = True 
elif birthMonth == 8 and (birthDay == 1 or birthDay < 23):
    z = 'Leo'
    validityCheck = True 
elif birthMonth == 8 and (birthDay == 23 or birthDay < 32):
    z = 'Virgo'
    validityCheck = True 
elif birthMonth == 9 and (birthDay == 1 or birthDay < 23):
    z = 'Virgo'
    validityCheck = True 
elif birthMonth == 9 and (birthDay == 23 or birthDay < 31):
    z = 'Libra'
    validityCheck = True 
elif birthMonth == 10 and (birthDay == 1 or birthDay < 23):
    z = 'Libra'
    validityCheck = True 
elif birthMonth == 10 and (birthDay == 23 or birthDay < 32):
    z = 'Scorpio'
    validityCheck = True 
elif birthMonth == 11 and (birthDay == 1 or birthDay < 22):
    z = 'Scorpio'
    validityCheck = True 
elif birthMonth == 11 and (birthDay == 22 or birthDay < 31):
    z = 'Sagittarius'
    validityCheck = True 
elif birthMonth == 12 and (birthDay == 1 or birthDay < 22):
    z = 'Sagittarius'
    validityCheck = True 
elif birthMonth == 12 and (birthDay == 22 or birthDay < 32):
    z = 'Capricorn'
    validityCheck = True 

if validityCheck == True:
    print(f'Your zodiac sign is {z}.')
else: 
    print('Wrong month or day.')