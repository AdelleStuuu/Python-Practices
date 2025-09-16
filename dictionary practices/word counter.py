print()
sentence =  input("Enter a sentence: ")
words = sentence.split()
wordCount = {}

for word in words: 
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

print()
print(wordCount)