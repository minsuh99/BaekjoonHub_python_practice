# Union-Find 이용
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

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)] # 각 노드의 부모를 담을 노드 (처음은 자기 자신)
    costs.sort(key=lambda x:x[2]) # 최소 비용이어야 하니, 비용이 작은 것부터 탐색하기 위함
    
    for i in range(len(costs)):
        if find(parents, costs[i][0]) == find(parents, costs[i][1]):
        # 연결하려는 노드들의 부모가 같다면 사이클 발생
            continue
        else:
            union(parents, costs[i][0], costs[i][1])
            answer += costs[i][2]
        
    return answer