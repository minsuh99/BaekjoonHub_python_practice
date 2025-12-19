import sys
input = sys.stdin.readline

N, k = map(int, input().split())
score = [int(i) for i in input().split()]

for i in range(N - 1):
    for j in range(i, N):
        if score[i] < score[j]:
            score[i], score[j] = score[j], score[i]

print(score[k-1])