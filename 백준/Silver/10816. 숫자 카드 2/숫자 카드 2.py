from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
my_dict = Counter([int(i) for i in input().split()])
M = int(input())
check_num = [int(i) for i in input().split()]
res = [0 for _ in range(M)]

for i in range(M):
    if check_num[i] in my_dict.keys():
        res[i] = my_dict[check_num[i]]

print(*res)