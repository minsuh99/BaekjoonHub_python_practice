import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:

        if len(scoville) < 2:
            return -1

        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)

        value = s1 + s2 * 2
        heapq.heappush(scoville, value)

        answer += 1

    return answer