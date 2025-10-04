import sys
input = sys.stdin.readline

MIN, MAX = map(int, input().split())
num_list = set()
cnt = MAX - MIN + 1

for i in range(2, int(MAX ** 0.5) + 1):
    if MIN % (i * i) == 0:
        start = MIN
    else:
        start = (MIN // (i * i) + 1) * (i * i)
    for j in range(start, MAX + 1, i * i):
        num_list.add(j)
    
print(cnt - len(num_list))