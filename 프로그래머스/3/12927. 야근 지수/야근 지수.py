import heapq


def solution(n, works):
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap, -work)
    
    print(works, heap)
    
    for _ in range(n):
        w = -heapq.heappop(heap)
        if w == 0:
            break
        heapq.heappush(heap, -(w - 1))
    
    answer = sum([(-i) ** 2 for i in heap])
    
    return answer