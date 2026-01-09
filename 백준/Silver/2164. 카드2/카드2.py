from collections import deque
N = int(input())
num_list = deque([int(i) for i in range(1, N + 1)])

while True:
    if len(num_list) == 1:
        print(num_list[0])
        exit()
    
    num_list.popleft()
    num_list.append(num_list.popleft())