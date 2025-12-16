N = int(input())
res = 0

while True:
    temp = res * (res + 1) // 2
    if temp <= N - 1 <= 6 * temp:
        break
    
    res += 1
    
print(res + 1)