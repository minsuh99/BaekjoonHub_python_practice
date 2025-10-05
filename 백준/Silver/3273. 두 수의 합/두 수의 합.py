import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(i) for i in input().split()]
num_list.sort()
x = int(input())

cnt = 0
idx1 = 0
idx2 = len(num_list) - 1

while idx1 < idx2:
    if num_list[idx1] + num_list[idx2] > x:
        idx2 -= 1
    elif num_list[idx1] + num_list[idx2] < x:
        idx1 += 1
    else:
        cnt += 1
        idx1 += 1

print(cnt)