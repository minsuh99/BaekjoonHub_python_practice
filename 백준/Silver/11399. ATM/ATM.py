N = int(input())
num_list = list(map(int, input().split()))
res_list = [0 for _ in range(N)]

num_list.sort()
res_list[0] = num_list[0]

for i in range(1, N):
    res_list[i] = res_list[i - 1] + num_list[i]

print(sum(res_list))
