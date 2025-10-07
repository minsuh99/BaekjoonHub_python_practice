import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rep_node = [i for i in range(N + 1)]

def find(a):
    if rep_node[a] == a:
        return a
    else:
        rep_node[a] = find(rep_node[a])
        return find(rep_node[a])

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        rep_node[b] = a

for _ in range(M):
    oper, a, b = map(int, input().split())
    
    if oper == 0:
        union(a, b)
    elif oper == 1:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")