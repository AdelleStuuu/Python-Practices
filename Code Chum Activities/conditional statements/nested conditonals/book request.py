age = int(input('Enter your age: '))
genre = input('Enter your genre preference (a for adventure, m for mystery, f for fantasy, s for science fiction): ')

if (8 <= age <= 12): 
    if genre == 'a': 
        print('The Adventures of Tom Sawyer')
    elif genre == 'm':
        print('Nancy Drew: The Secret of the Old Clock')
elif age >= 13:
    if genre == 'f':
        print('Harry Potter and the Sorcerer\'s Stone')
    elif genre == 's':
        print('Ender\'s Game')
else: 
    print('No recommendation available')