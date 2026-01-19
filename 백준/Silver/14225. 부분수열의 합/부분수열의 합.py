import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N= int(input())
num_list = list(map(int, input().split()))
num_list.sort()
res_sum = set()


def backtrack(start, res_list):
    global res_sum
    if res_list:
        res_sum.add(sum(res_list))

    for i in range(start, N):
        res_list.append(num_list[i])
        backtrack(i + 1, res_list)
        res_list.pop()

backtrack(0, [])

res = 1
while True:
    if res not in res_sum:
        print(res)
        exit()
    res += 1