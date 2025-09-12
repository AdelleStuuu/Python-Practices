vowels = ['a','e','i','o','u']
print()
while True: 
    character = input('Enter a letter: ')
    characterLength = len(character)
    if characterLength > 1:
        print('Character count is greater than 1.')
        print()
    elif character.isdigit():
        print('Character can not be a number')
        print()
    else: 
        if character.lower() in vowels:
            print('The letter is a vowel!')
        else:
            print('The letter is a consonant!') 
        print()
        break 
    