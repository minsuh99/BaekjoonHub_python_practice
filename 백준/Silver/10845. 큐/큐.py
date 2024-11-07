import sys

n = int(sys.stdin.readline())
my_list = list()

for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        op, num = command[0], int(command[1])
        if op == 'push':
            my_list.append(num)
    else:
        op = command[0]
        if op == 'pop':
            print(my_list.pop(0) if len(my_list) != 0 else -1)
        elif op == 'size':
            print(len(my_list))
        elif op == 'empty':
            print(1 if len(my_list)==0 else 0)
        elif op == 'front':
            print(my_list[0] if len(my_list) != 0 else -1)
        elif op == 'back':
            print(my_list[-1] if len(my_list) != 0 else -1)