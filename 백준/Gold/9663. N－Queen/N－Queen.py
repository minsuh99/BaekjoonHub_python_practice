import sys
input = sys.stdin.readline

N = int(input())
row = [-1 for _ in range(N)]
res = 0

def backtracking(r):
    global res
    if r == N:
        res += 1
        return

    for c in range(N):
        flag = True
        for prev in range(r):
            if row[prev] == c:
                flag = False
                break
            if abs(row[prev] - c) == r - prev:
                flag = False
                break

        if not flag:
            continue

        row[r] = c
        backtracking(r + 1)
        row[r] = -1

backtracking(0)
print(res)
