N = int(input())
num_list = list(map(int, input().split()))
M = max(num_list)

res = [i/M * 100 for i in num_list]
print(sum(res) / len(res))