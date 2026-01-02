N = int(input())
my_list = [int(i) for i in input().split()]
res = -1

for i in range(N - 1, 0, -1):
    if my_list[i - 1] > my_list[i]:
        split_idx = i - 1
        
        left = my_list[:split_idx]
        right = my_list[split_idx:]
        
        temp = 0
        for j in range(1, len(right)):
            if right[0] > right[j]:
                if right[j] > temp:
                    temp = right[j]
                    switch_idx = j
        
        right[0], right[switch_idx] = right[switch_idx], right[0]

        res = left + [right[0]] + right[1:][::-1]
        print(*res)
        exit()
        
    
print(res)