import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
res = 0


def backtrack(start, res_list):
    global res
    if res_list and sum(res_list) == S:
        res += 1

    for i in range(start, N):
        res_list.append(num_list[i])
        backtrack(i + 1, res_list)
        res_list.pop()

backtrack(0, [])
print(res)