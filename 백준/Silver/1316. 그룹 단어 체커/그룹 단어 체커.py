N = int(input())
cnt = N

for _ in range(N):
    word = input()
    temp = []
    
    for i in range(len(word)):
        if word[i] not in temp:
            temp.append(word[i])
        elif word[i] != word[i-1]:
            cnt -= 1
            break

print(cnt)