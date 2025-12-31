N = int(input())
my_list = [int(i) for i in input().split()]

for i in range(N - 1, 0, -1):
    if my_list[i] > my_list[i - 1]:
        split_idx = i - 1
        left = my_list[:split_idx]
        right = my_list[split_idx:]
        
        temp = N + 1
        for j in range(1, len(right)):
            if right[j] > right[0] and right[j] < temp:
                temp = right[j]
                switch_idx = j
        
        right[0], right[switch_idx] = right[switch_idx], right[0]
        res_list = left + [right[0]] + sorted(right[1:])
        print(*res_list)
        exit()
        
print(-1)