x = int(input())
n = int(input())

res = 0

for _ in range(n):
    a, b = map(int, input().split())
    res += a*b

if x == res:
    print("Yes")
else:
    print("No")