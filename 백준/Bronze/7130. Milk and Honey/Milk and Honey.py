m, h = map(int, input().split())
n = int(input())
happiness = 0

for _ in range(n):
    c, b = map(int, input().split())
    happiness += max(m * c, h * b)

print(happiness)