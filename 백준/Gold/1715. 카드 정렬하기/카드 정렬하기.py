from queue import PriorityQueue
import sys
input = sys.stdin.readline
my_queue = PriorityQueue()
res = 0

N = int(input())
for _ in range(N):
    my_queue.put(int(input()))

while my_queue.qsize() != 1:
    card1_size = my_queue.get()
    card2_size = my_queue.get()
    new_size = card1_size + card2_size
    res += new_size    
    my_queue.put(new_size)

print(res)