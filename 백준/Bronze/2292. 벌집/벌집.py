n = int(input())
res = 1
path_num = 1

while True:
    if n <= res:
        break
    else:
        res += path_num * 6
        path_num += 1
print(path_num)