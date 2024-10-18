l = int(input())
word = input()
res = 0

for i in range(len(word)):
    res += (ord(word[i]) - ord('a') + 1) * (31 ** i)

print(res % 1234567891)