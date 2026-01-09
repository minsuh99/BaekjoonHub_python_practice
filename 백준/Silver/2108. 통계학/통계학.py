from collections import Counter
import math
import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
num_dict = Counter(num_list)
most_frec = [k for k in num_dict.keys() if num_dict[k] == max(num_dict.values())]
if len(most_frec) >= 2:
    most_frec.sort()

print(math.floor((sum(num_list) / len(num_list)) + 0.5))
print(num_list[int(N // 2)])
print(most_frec[1] if len(most_frec) >= 2 else most_frec[0])
print(num_list[-1] - num_list[0])