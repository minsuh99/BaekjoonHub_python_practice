import sys
input = sys.stdin.readline

N = int(input())
my_list = [int(i) for i in input().split()]
my_list.sort()
cnt = 0

for k in range(len(my_list)):
    i = 0
    j = N - 1
    temp_sum = 0

    while i < j:
        temp_sum = my_list[i] + my_list[j]
        if temp_sum == my_list[k]:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif temp_sum > my_list[k]:
            j -= 1
        else:
            i += 1
            
print(cnt)