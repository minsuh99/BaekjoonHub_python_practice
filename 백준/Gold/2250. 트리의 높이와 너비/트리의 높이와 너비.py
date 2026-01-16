import sys
input = sys.stdin.readline

N = int(input())

left = [-1 for _ in range(N + 1)]
right = [-1 for _ in range(N + 1)]
roots = [0 for _ in range(N + 1)]

for _ in range(N):
    node, l, r = map(int, input().split())
    left[node] = l
    right[node] = r
    if l != -1:
        roots[l] = node
    if r != -1:
        roots[r] = node

root = 0
for i in range(1, N + 1):
    if roots[i] == 0:
        root = i
        break

INF = 10**9
min_x = [INF for _ in range(N + 1)]
max_x = [0 for _ in range(N + 1)]

x = 1
def inorder(cur, depth):
    global x
    if cur == -1:
        return
    inorder(left[cur], depth + 1)

    min_x[depth] = min(min_x[depth], x)
    max_x[depth] = max(max_x[depth], x)
    x += 1

    inorder(right[cur], depth + 1)

inorder(root, 1)

best_level = 0
best_width = 0

for level in range(1, len(min_x)):
    if min_x[level] == INF:
        continue

    width = max_x[level] - min_x[level] + 1

    if width > best_width:
        best_width = width
        best_level = level

print(best_level, best_width)