alphabet = [-1 for _ in range(26)]
word = input()

for i in range(len(word)):
    if alphabet[ord(word[i]) - ord('a')] == -1:
        alphabet[ord(word[i]) - ord('a')] = i

print(*alphabet)