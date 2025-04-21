s = input()
res = set()

for i in range(len(s)):
    for j in range(1, len(s) - i + 1):
        res.add(s[i:i+j])

print(len(res))