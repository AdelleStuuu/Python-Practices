initialWord = str(input('Enter a word here: '))
reversedWord = initialWord[::-1]

isPalindrome = 'Yes this is a Palindrome' if initialWord.upper() == reversedWord.upper() else 'No this is not a Palindrome'

print(isPalindrome)

