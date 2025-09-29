import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
S = [0 for _ in range(N)]
S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]
    
S = [0] + S

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i-1])
