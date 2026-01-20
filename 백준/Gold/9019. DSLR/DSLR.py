from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    opers = ["D", "S", "L", "R"]
    visited = [False for _ in range(10000)]
    visited[A] = True
    
    queue = deque([(A, "")])
    
    while queue:
        num, res = queue.popleft()
        if num == B:
            print(res)
            break
        
        for oper in opers:
            if oper == "D":
                temp = (num * 2) % 10000                
                if visited[temp]:
                   continue
        
            elif oper == "S":
                temp = (num + 10000 - 1) % 10000
                if visited[temp]:
                   continue
            
            elif oper == "L":
                temp = (num % 1000) * 10 + (num // 1000)
                if visited[temp]:
                   continue
        
            elif oper == "R":
                temp = (num // 10) + (num % 10) * 1000
                if visited[temp]:
                   continue
            
            new_num = temp
            visited[new_num] = True
            queue.append((new_num, res + oper))
            