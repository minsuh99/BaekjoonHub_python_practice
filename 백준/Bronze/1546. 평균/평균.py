n = int(input())
num_list = [int(i) for i in input().split()]

max_num = max(num_list)
new_list = [(i/max_num) * 100 for i in num_list]

print(sum(new_list) / n)