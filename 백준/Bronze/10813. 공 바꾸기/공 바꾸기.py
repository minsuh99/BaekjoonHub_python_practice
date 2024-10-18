n, m = map(int, input().split())
num_list = list(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    num_list[a-1], num_list[b-1] = num_list[b-1], num_list[a-1]

for num in num_list:
    print(num, end=" ")