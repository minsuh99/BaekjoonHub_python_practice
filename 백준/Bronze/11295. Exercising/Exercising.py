import sys

user = 1
while True:
    l = int(sys.stdin.readline().strip())
    if l == 0:
        break
    else:
        print(f'User {user}')
    
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        print(f'{int(sys.stdin.readline().strip()) * l / 100000:.5f}')
    
    user += 1