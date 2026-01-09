from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    printer_queue = deque([(int(num), int(i)) for i, num in enumerate(input().split())])
    
    target = max(printer_queue)[0]
    cnt = 1
    
    while True:
        if printer_queue[0][0] < target:
            printer_queue.rotate(-1)
            continue
        elif printer_queue[0][0] == target:
            if printer_queue[0][1] == M:
                print(cnt)
                break
            else:
                printer_queue.popleft()
                target = max(printer_queue)[0]
                cnt += 1
