import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
W = []
for _ in range(N):
    W.append([int(i) for i in input().split()])

visited = [False for _ in range(N)]
res = 10 ** 7

# 시작점을 고정해도 같은 해가 나옴
# 0 -> 1 -> 2 -> 3 -> 0 이나
# 1 -> 2 -> 3 -> 0 -> 1 이나 같은 비용을 계산함
# 시작을 0으로 고정하는게 좋아보임


def backtrack(res_list):
    global res
    # 시작점 0 고정
    if len(res_list) == 0:
        res_list.append(0)
        visited[0] = True
        
    if len(res_list) == N:
        res_list.append(res_list[0])
        temp = 0
        for i in range(len(res_list) - 1):
            temp += W[res_list[i]][res_list[i + 1]]
        
        res = min(res, temp)
        res_list.pop()
        return
    
    for i in range(1, N):
        if visited[i]:
            continue
        
        if W[res_list[-1]][i] == 0:
            continue
        
        if len(res_list) == N - 1 and W[i][res_list[0]] == 0:
            continue
        
        visited[i] = True
        res_list.append(i)
        backtrack(res_list)
        res_list.pop()
        visited[i] = False

backtrack([])
print(res)
        