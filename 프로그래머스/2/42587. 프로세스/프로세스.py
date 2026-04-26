from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    sort_priorities = sorted(priorities)

    while queue:
        if queue[0][1] == sort_priorities[-1]:
            sort_priorities.pop()
            idx, _ = queue.popleft()
            answer += 1
            if idx == location:
                return answer
        else:
            queue.rotate(-1)