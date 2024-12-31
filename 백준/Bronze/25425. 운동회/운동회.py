N, M, a, K = map(int, input().split())

if (a - K) % M == 0:
    max_rank = int((a - K) / M )+ 1
else:
    max_rank = int((a- K) / M)+ 2

if (a - K) >= (N - 1):
    min_rank = N
else:
    min_rank = a - K + 1

print(min_rank, max_rank)