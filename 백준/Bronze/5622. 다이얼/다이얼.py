dial = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], 
        ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"],
        ["T", "U", "V"], ["W", "X", "Y", "Z"]]

word = input()
res = 0

for w in word:
    for i, lis in enumerate(dial):
        if w in lis:
            res += 3 + i
            break

print(res)