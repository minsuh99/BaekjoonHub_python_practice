n, m = map(int, input().split())
num_list = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        num_list[idx] = k

for num in num_list:
    print(num, end=" ")