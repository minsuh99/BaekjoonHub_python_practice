n, k = map(int, input().split())

num_list = [int(i) for i in input().split()]

res = sum(sorted(num_list, reverse=True)[:k]) - sum(range(1, k))
print(res)