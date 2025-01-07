n = int(input())
for _ in range(n):
    num = int(input())
    num2 = num
    while True:
        print(num2)
        
        if num2 // 100 == 0:
            break
        
        num2 = (num2 // 10) - (num2 % 10)
    
    if num2 % 11 == 0:
        print(f'The number {num} is divisible by 11.')
    else:
        print(f'The number {num} is not divisible by 11.')
    print()