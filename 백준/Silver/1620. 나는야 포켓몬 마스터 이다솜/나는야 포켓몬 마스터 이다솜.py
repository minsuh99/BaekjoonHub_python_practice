import sys
pok_dict = dict()
pok_dict2 = dict()
n, m = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    name = str(sys.stdin.readline().strip())
    pok_dict[i] = name
    pok_dict2[name] = i

for _ in range(m):
    check = sys.stdin.readline().strip()
    if check.isdigit():
        print(pok_dict[int(check)])
    else:
        print(pok_dict2[check])