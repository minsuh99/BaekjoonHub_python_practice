from itertools import permutations

N = int(input())
A = [int(i) for i in input().split()]

all_permu = list(permutations(A))
res = 0

for my_list in all_permu:
    temp = 0
    for i in range(len(my_list) - 1):
        temp += abs(my_list[i] - my_list[i + 1])
    
    res = max(res, temp)

print(res)