character1 = input('Enter character 1: ')
character2 = input('Enter character 2: ')
unicode1 = ord(character1)
unicode2 = ord(character2)

if unicode1 < unicode2: 
    print(f'The lesser character is: {character1}') 
else:
    print(f'The lesser character is: {character2}')