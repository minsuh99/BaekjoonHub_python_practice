import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

alpha_sum = [[0] * (len(S) + 1) for _ in range(26)]

for i in range(len(S)):
    for j in range(26):
        alpha_sum[j][i + 1] = alpha_sum[j][i]
    alpha_sum[ord(S[i]) - ord('a')][i + 1] += 1


for _ in range(q):
    alpha, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    print(alpha_sum[(ord(alpha) - ord('a'))][r+1] - alpha_sum[(ord(alpha) - ord('a'))][l])