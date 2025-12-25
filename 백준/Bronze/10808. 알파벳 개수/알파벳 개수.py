my_list = [0 for _ in range(26)]
word = input()

for w in word:
    my_list[ord(w) - ord('a')] += 1

print(*my_list)