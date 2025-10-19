"""
Word Occurrences
Estimate: 13 minutes
Actual: 1 hour 15 minutes
"""

words = {}

sentence = input("Text: ").split()
sentence.sort()
for word in sentence:
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

max_length = max(len(word) for word in list(words.keys()))

for word in words:
    print(f"{word:{max_length}} : {words[word]}")
