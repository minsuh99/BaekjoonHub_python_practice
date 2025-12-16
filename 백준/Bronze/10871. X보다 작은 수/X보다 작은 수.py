N, X = map(int, input().split())
A = [i for i in list(map(int, input().split())) if i < X]

print(*A)

