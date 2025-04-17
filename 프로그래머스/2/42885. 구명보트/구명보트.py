def solution(people, limit):
    answer = 0
    people = sorted(people)
    boat = 0
    
    left_idx = 0
    right_idx = len(people) - 1
    
    while left_idx <= right_idx:
        boat += people[right_idx]
        right_idx -= 1
        
        if people[left_idx] <= limit - boat:
            left_idx += 1
        answer += 1
        
        boat = 0

    return answer