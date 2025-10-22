def palindrome(word):
    # reversing a string by using
    # the join function with the seperator ""
    # and the word being inside the reversed function
    reversedString = "".join(reversed(word))
    # checks if the arg word is equal to 
    # the variable reversedString
    if word.lower() == reversedString.lower():
        isPalindrome = True
    else:
        isPalindrome = False
    # return the boolean value
    return isPalindrome

print()
# defined
print(palindrome("racecar"))
print(palindrome("muerte"))
print()
# user input 
word = input("Enter a word here: ")
print(palindrome(word))
print()