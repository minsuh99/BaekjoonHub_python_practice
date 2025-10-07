import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

city = [[0 for _ in range(N)] for _ in range(N)] # 1, 2, 3번 도시로 하나, 편의상 0, 1, 2로 설정.
parent = [i for i in range(N)]

for i in range(N):
    city[i] = list(map(int, input().split()))

check_route = list(map(int, input().split()))

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            union(i, j)

check_route = set([find(i - 1) for i in check_route])

    
print("NO" if len(check_route) > 1 else "YES")