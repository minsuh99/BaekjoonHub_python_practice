import sys
input = sys.stdin.readline

N = int(input())
meeting = []

for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x:(x[1], x[0]))

cur_end = -1
res = 0
for time in meeting:
    if time[0] >= cur_end:
        cur_end = time[1]
        res += 1

print(res)