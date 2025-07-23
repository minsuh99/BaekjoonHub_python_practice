import sys

stack = []

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    match int(command[0]):
        case 1:
            stack.append(int(command[1]))
        case 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        case 3:
            print(len(stack))
        case 4:
            if stack:
                print(0)
            else:
                print(1)
        case 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
                
    