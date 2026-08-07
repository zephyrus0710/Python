text = input("Enter a sentence: ")

words = text.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for word in frequency:
    print(word, ":", frequency[word])