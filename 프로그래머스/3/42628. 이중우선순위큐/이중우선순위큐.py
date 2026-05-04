from collections import deque


def solution(operations):
    answer = []
    queue = deque([])
    
    for operation in operations:
        cmd, num = map(str, operation.split())
        num = int(num)
        if cmd == "I":
            if not queue or queue[-1] < num:
                queue.append(num)
            elif queue[0] > num:
                queue.appendleft(num)
        
        elif cmd == "D":
            if queue:
                if num == 1:
                    queue.pop()
                elif num == -1:
                    queue.popleft()
    
    answer = [queue[-1], queue[0]] if queue else [0, 0]
    
    return answer