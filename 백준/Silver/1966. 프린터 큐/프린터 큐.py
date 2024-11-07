import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    importance = [int(i) for i in sys.stdin.readline().split()]
    
    my_list = deque([(i, importance[i]) for i in range(n)])
    res_list = []
    importance.sort()
    
    next_importance = importance[-1]
    while True:
        if my_list[0][1] != next_importance:
            my_list.rotate(-1)
        else:
            res_list.append(my_list.popleft())
            if len(my_list) != 0:
                importance.pop()
                next_importance = importance[-1]
            else:
                break
    
    res_list = [i[0] for i in res_list]
    print(res_list.index(m) + 1)