import sys

m = int(sys.stdin.readline())
my_set = set()

for _ in range(m):
    command = list(sys.stdin.readline().split())
    
    if len(command) == 1:
        if command[0] == 'all':
            my_set = set([int(i) for i in range(1, 21)])
        elif command[0] == 'empty':
            my_set.clear()
    else:
        operator, num = command[0], int(command[1])
        if operator == 'add':
            my_set.add(num)
            
        elif operator == 'remove':
            my_set.discard(num)
            
        elif operator == 'check':
            print(1 if num in my_set else 0)
            
        elif operator == 'toggle':
            if int(num) not in my_set:
                my_set.add(num)
            else:
                my_set.discard(num)