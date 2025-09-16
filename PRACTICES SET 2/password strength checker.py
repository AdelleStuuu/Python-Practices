print()
while True:
    password = input('Enter your password here!: ')
    if password == '':
        print('Password can\'t be null!')
    else:
        break
passwordSliced = list(password)
numbers = str([1,2,3,4,5,6,7,8,9,0])
strengthPoints = 0
print()
for bigLetters in passwordSliced:
    if bigLetters.isupper():
        strengthPoints += 1

for numChecking in passwordSliced:
    if numChecking in numbers:
        strengthPoints += 2 

for specialCharacters in passwordSliced:
    if not(specialCharacters.isalpha() or specialCharacters.isdigit()):
        strengthPoints += 3
        
if len(password) >= 12:
    strengthPoints += 10
elif len(password) >= 8:
    strengthPoints += 5

if strengthPoints > 15:
    print('Ooo, strong password!')
elif strengthPoints > 10:
    print('Hmm, its an okay password!')
else:
    print('oomf, that password kinda weak!')
print()