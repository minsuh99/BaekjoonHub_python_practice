import sys
input = sys.stdin.readline

N = int(input())
chong_list = set()

for _ in range(N):
    name1, name2 = map(str, input().rstrip().split())
    if name1 == "ChongChong" or name2 == "ChongChong":
        chong_list.add(name1)
        chong_list.add(name2)
    elif name1 in chong_list:
        chong_list.add(name2)
    elif name2 in chong_list:
        chong_list.add(name1)
    else:
        continue

print(len(chong_list))