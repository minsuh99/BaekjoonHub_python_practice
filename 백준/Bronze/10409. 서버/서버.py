n, T = map(int, input().split())
num_list = list(map(int, input().split()))

partial_sum = [0 for _ in range(n)]+[50*500]
partial_sum[0] = num_list[0]

for i in range(1, n):
    partial_sum[i] = partial_sum[i - 1] + num_list[i]

for i, num in enumerate(partial_sum):
    if num > T:
        print(i)
        break