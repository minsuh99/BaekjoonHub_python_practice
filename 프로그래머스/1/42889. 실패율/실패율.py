def solution(N, stages):
    answer = []
    challenge_people = len(stages)
    fail_ratio = []
    
    for stage in range(1, N+1):
        not_clear_people = stages.count(stage)
        pass_people = challenge_people - not_clear_people
        
        if challenge_people != 0:
            fail_ratio.append((stage, not_clear_people / challenge_people))
        else:
            fail_ratio.append((stage, 0))
        challenge_people -= not_clear_people
    
    temp = [c[0] for c in sorted(fail_ratio, key=lambda x: (-x[1], x[0]))]
                
    return temp