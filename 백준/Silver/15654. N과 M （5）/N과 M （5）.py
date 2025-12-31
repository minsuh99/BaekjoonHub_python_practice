import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
my_list = sorted([int(i) for i in input().split()])
visited = [False for _ in range(N)]

def backtrack(res_list):
    if len(res_list) == M:
        print(*res_list)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        res_list.append(my_list[i])
        visited[i] = True
        backtrack(res_list)
        visited[i] = False
        res_list.pop()

backtrack([])