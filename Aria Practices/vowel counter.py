def count_vowels(word):
    vowels = ['A','E','I','O','U']
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

chosenWord = input("Enter a word: ")
vowel_count = count_vowels(chosenWord.upper())
print(f"Number of vowels in '{chosenWord}': {vowel_count}")

