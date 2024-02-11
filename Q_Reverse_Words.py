s = input()
words = s.split()
# reversed_words = [word[::-1] for word in words]
# code in details
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])

reversed_s = ' '.join(reversed_words)
print(reversed_s)

