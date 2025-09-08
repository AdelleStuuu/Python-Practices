vowel = ('a','e','i','o','u')
word = input('Enter a character: ')

if word.lower() in vowel:
    print('The character is a vowel.')
else:
    print('The character is a consonant.')