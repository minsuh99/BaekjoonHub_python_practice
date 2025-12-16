N, M = map(int, input().split())
A, B = [], []
C = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

C = [[a+b for a, b in zip(A[j], B[j])] for j in range(N)]

for row in C:
    print(*row)