from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    cur_w = 0
    
    while people:
        if cur_w == 0:
            cur_w += people.pop()
        else:
            if people[0] + cur_w <= limit:
                cur_w = 0
                people.popleft()
            else:
                cur_w = people.pop()
            answer += 1
    if cur_w > 0:
        answer += 1
    return answer