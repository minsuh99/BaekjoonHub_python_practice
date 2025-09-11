import sys
input = sys.stdin.readline

n = int(input())
names = []
answer = []

for _ in range(n):
    names.append(input().rstrip())

cur_idx = 0
while cur_idx < len(names[0]):
    temp = set()
    for name in names:
        temp.add(name[cur_idx])
    if len(temp) == 1:
        answer.append(list(temp)[0])
    else:
        answer.append("?")
    cur_idx += 1
print("".join(answer))