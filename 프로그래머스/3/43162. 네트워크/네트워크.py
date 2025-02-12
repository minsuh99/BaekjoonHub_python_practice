# Union-Find 스스로 짜보기
def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x, y = min(x, y), max(x, y)
    root1 = find(parents, x)
    root2 = find(parents, y)
    
    parents[root2] = root1

def solution(n, computers):
    computers_edge = []
    for i in range(len(computers)):
        for j in range(i, len(computers[0])):
            if i == j:
                continue
            if computers[i][j] == 1:
                computers_edge.append([i, j])
                
    parents = [i for i in range(n)]
    
    for edge in computers_edge:
        if find(parents, edge[0]) == find(parents, edge[1]):
            continue
        else:
            union(parents, edge[0], edge[1])
    
    return len(set(list([find(parents, i) for i in range(n)])))