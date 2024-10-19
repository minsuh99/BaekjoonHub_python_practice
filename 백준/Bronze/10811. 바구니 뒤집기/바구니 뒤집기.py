n, m = map(int, input().split())
num_list = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    temp = num_list[i-1:j]
    temp.reverse()
    num_list[i-1:j] = temp
    
for num in num_list:
    print(num, end=" ")