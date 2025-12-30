N = int(input())
A = [int(i) for i in input().split()]
dp1 = [1 for _ in range(N)] # 증가만하는 수열
dp2 = [1 for _ in range(N)] # 감소만하는 수열

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N-1, -1, -1): # 감소는 오른쪽에서부터 계산
    for k in range(N-1, i, -1):
        if A[i] > A[k]:
            dp2[i] = max(dp2[i], dp2[k] + 1)
    
print(max([num1 + num2 - 1 for num1, num2 in zip(dp1, dp2)])) 
# 자기자신을 기준으로 왼쪽에서 증가하고 있는 부분과, 오른쪽에서 감소하고 있는 부분의 길이를 더해 가장 긴 수열을 찾음
# -1은 자기자신을 2번 세고 있어서