s = input().strip()
words = s.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

print(' '.join(reversed_words))
