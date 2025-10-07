import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth = [int(i) for i in input().split()[1:]]
parent = [i for i in range(N + 1)]
party_list = []
res = 0

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

for _ in range(M):
    party = [int(i) for i in input().split()[1:]]
    party_list.append(party)
    
    if len(party) == 1:
        continue
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])

for party in party_list:
    temp = find(party[0])
    flag = True
    for p in truth:
        if temp == find(p):
            flag = False
            break
    if flag:
        res += 1

print(res)