character = input('Enter character: ')
isLetter = character.isalpha()
isNumber = character.isnumeric()

if not(isLetter or isNumber): 
    print('Character is a special character.')