birthMonth = int(input('Enter your birth month [1-12]: '))
birthDay = int(input('Enter you birth day: '))
validityCheck = True
zodiac = ''

if birthMonth == 1: 
    if birthDay == 1 or birthDay < 20: 
        zodiac = 'Capricorn'
    elif birthDay < 32:
        zodiac = 'Aquarius'
elif birthMonth == 2:
    if birthDay == 1 or birthDay < 19:
        zodiac = 'Aquarius'
    elif birthDay < 30:
        zodiac = 'Pisces'
elif birthMonth == 3:
    if birthDay == 11 or birthDay < 20:
        zodiac = 'Pisces'
    elif birthDay < 32:
        zodiac = 'Aries'
elif birthMonth == 4:
    if birthDay == 1 or birthDay < 20:
        zodiac = 'Aries'
    elif birthDay < 31:
        zodiac = 'Taurus'
elif birthMonth == 5:
    if birthDay == 1 or birthDay < 20:
        zodiac = 'Taurus'
    elif birthDay < 32:
        zodiac = 'Gemini'
elif birthMonth == 6:
    if birthDay == 1 or birthDay < 21:
        zodiac = 'Gemini'
    elif birthDay < 31:
        zodiac = 'Cancer'
elif birthMonth == 7:
    if birthDay == 1 or birthDay < 23:
        zodiac = 'Cancer'
    elif birthDay < 32:
        zodiac = 'Leo'
elif birthMonth == 8:
    if birthDay == 1 or birthDay < 23:
        zodiac = 'Leo'
    elif birthDay < 32:
        zodiac = 'Virgo'
elif birthMonth == 9:
    if birthDay == 1 or birthDay < 23:
        zodiac = 'Virgo'
    elif birthDay < 31:
        zodiac = 'Libra'
elif birthMonth == 10:
    if birthDay == 1 or birthDay < 23:
        zodiac = 'Libra'
    elif birthDay < 32:
        zodiac = 'Scorpio'
elif birthMonth == 11:
    if birthDay == 1 or birthDay < 22:
        zodiac = 'Scorpio'
    elif birthDay < 31:
        zodiac = 'Sagittarius'
elif birthMonth == 12:
    if birthDay == 1 or birthDay < 22:
        zodiac = 'Sagittarius'
    elif birthDay < 32:
        zodiac = 'Capricorn'
else:
    validityCheck = False

if zodiac == '':
    validityCheck = False

if validityCheck == True:
    print(f'Your zodiac sign is {zodiac}.')
else:
    print('Wrong month or day.')