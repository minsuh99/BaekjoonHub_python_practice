import sys
sys.setrecursionlimit(10 ** 9)
from itertools import product

N, M = map(int, input().split())
# my_list = [int(i) for i in range(1, N + 1)]
# for res in list(product(my_list, repeat=M)):
#     print(*res)

def backtrack(res_list):
    if len(res_list) == M:
        print(*res_list)
        return
    
    for i in range(N):
        res_list.append(i + 1)
        backtrack(res_list)
        res_list.pop()

backtrack([])