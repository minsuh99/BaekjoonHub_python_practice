from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())

my_queue = PriorityQueue()

for _ in range(N):    
    x = int(input())
    if x == 0:
        if my_queue.empty():
            print(0)
        else:
            print(my_queue.get())
    
    else:
        my_queue.put(x)