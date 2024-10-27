n, m = map(int, input().split())

A = [[0]*m]*n
B = [[0]*m]*n

for i in range(n):
    A[i] = [int(i) for i in input().split()]

for i in range(n):
    B[i] = [int(i) for i in input().split()]

for i in range(n):
    for j in range(m):
        print(A[i][j] + B[i][j], end=" ")
    print()