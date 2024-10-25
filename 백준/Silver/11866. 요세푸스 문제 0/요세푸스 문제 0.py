n, k = map(int, input().split())
my_list = [int(i) for i in range(1, n+1)]
res_list = []
i = k-1

while True:
    res_list.append(str(my_list[i]))
    my_list.remove(my_list[i])
    
    if len(my_list) == 0:
        break
    
    i += k - 1
    i %= len(my_list)

print(f'<{", ".join(res_list)}>')