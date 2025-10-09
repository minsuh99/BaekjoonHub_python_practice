from collections import deque

def solution(priorities, location):
    answer = 0
    new_prior = deque([(i, priority) for i, priority in enumerate(priorities)])
    priorities.sort()

    while new_prior:
        if new_prior[0][1] != priorities[-1]:
            new_prior.rotate(-1)
        else:
            loc, _ = new_prior.popleft()
            priorities.pop()
            answer += 1
            if loc == location:
                break

    return answer