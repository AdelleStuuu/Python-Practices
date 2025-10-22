def palindrome(word):
    reversedString = "".join(reversed(word))
    if word.lower() == str(reversedString).lower():
        isPalindrome = True
    else:
        isPalindrome = False
    
    return isPalindrome

print(palindrome("racecar"))
print(palindrome("muerte"))