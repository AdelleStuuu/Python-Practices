print()
sentence =  input("Enter a sentence: ")
words = sentence.split()
wordCount = {}

for word in words: 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print()
print(word_count)