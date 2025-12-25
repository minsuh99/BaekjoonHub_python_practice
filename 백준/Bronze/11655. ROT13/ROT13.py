S = input()
res = ""

for s in S:
    if s.isalpha():
        if s.islower():
            res += chr(ord('a') + ((ord(s) - ord('a') + 13) % 26))
        elif s.isupper():
            res += chr(ord('A') + ((ord(s) - ord('A') + 13) % 26))
    else:
        res += s

print(res)