import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
my_list = sorted([int(i) for i in input().split()])

def backtrack(start, res_list):
    if len(res_list) == M:
        print(*res_list)
        return
    
    for i in range(start, N):       
        res_list.append(my_list[i])
        backtrack(i + 1, res_list)
        res_list.pop()

backtrack(0, [])