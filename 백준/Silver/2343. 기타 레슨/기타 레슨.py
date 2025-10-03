import sys
input = sys.stdin.readline

N, M = map(int, input().split())
my_list = [int(i) for i in input().split()]

start = max(my_list)
end = sum(my_list)
ans = 0

while start <= end:
    mid = int((start + end) / 2)
    temp_sum = 0
    blue_rey = 0
    for i in range(len(my_list)):
        if temp_sum + my_list[i] > mid:
            temp_sum = 0
            blue_rey += 1
        temp_sum += my_list[i]
    if temp_sum != 0:
        temp_sum = 0
        blue_rey += 1
    if blue_rey > M:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)