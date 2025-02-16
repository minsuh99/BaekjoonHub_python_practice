k, n= map(int, input().split())   
l = [int(input()) for _ in range(k)]

start = 1   
end = max(l)   

while start <= end:   
    mid = (start + end) // 2   
    res = 0   

    for l_ in l:
        res += l_ // mid
    
    if res >= n:   
        start = mid + 1   
    else:   
        end = mid - 1   

print(end)