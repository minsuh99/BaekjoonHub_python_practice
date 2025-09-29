import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
my_list = [int(i) for i in input().split()]
my_list.sort()

start_idx = 0
end_idx = N -1
temp_sum = 0
cnt = 0

while start_idx < end_idx:
    temp_sum = my_list[start_idx] + my_list[end_idx]
    if temp_sum > M:
        end_idx -= 1
    elif temp_sum == M:
        cnt += 1
        start_idx += 1
        end_idx -= 1
    else:
        start_idx += 1

print(cnt)