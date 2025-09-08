import math 

birthYear = int(input('Enter your birth year: ')) 
currentYear = int(input('Enter the current year: '))
age = currentYear - birthYear
age2 = birthYear - currentYear

# Check if birth year is less than current year to avoid negative age
# This is needed because of a codechum bug that allows negative input
if birthYear < currentYear:
    sqroot = math.sqrt(age)
    if sqroot.is_integer():
        print('Your age is a perfect square.')
    else:
        print('Your age is not a perfect square.')
else:
    sqroot2 = math.sqrt(age2)
    if sqroot2.is_integer():
        print('Your age is a perfect square.')
    else:
        print('Your age is not a perfect square.')