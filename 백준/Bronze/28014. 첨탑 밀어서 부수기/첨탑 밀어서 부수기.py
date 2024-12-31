N = int(input())
height = [int(i) for i in input().split()]

res = 0
for i in range(N):
    if (i == N - 1) or (i != N - 1 and height[i] <= height[i+1]):
        res += 1

print(res)