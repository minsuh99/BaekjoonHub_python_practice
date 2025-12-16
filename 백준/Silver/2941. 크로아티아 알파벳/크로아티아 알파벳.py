my_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
cnt = 0
i = 0

while True:
    if i >= len(word):
        break
    
    if word[i:i+2] in my_list:
        i += 2
    elif word[i:i+3] in my_list:
        i += 3
    else:
        i += 1
    cnt += 1

print(cnt)