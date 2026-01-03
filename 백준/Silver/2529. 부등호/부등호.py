import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

k = int(input())
inequal = input().rstrip().split()

res_max = ""
res_min = None
visited = [False for _ in range(10)]

def valid(a, b, op):
    return a < b if op == '<' else a > b

def backtrack(res):
    global res_max, res_min

    if len(res) == k + 1:
        s = "".join(map(str, res))
        if res_min is None or s < res_min:
            res_min = s
        if s > res_max:
            res_max = s
        return

    for d in range(10):
        if visited[d]:
            continue
        if len(res) == 0 or valid(res[-1], d, inequal[len(res)-1]):
            visited[d] = True
            backtrack(res + [d])
            visited[d] = False

backtrack([])

print(res_max)
print(res_min)
