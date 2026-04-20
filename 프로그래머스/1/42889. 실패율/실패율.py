from collections import Counter


def solution(N, stages):
    fail_ratio = [[i + 1, 0] for i in range(N)]
    stage_count = Counter(stages)
    cur_people = len(stages)
    
    for i in range(N):
        if i + 1 in stage_count:
            fail_ratio[i][1] = stage_count[i + 1] / cur_people
            cur_people -= stage_count[i + 1]
    
    fail_ratio.sort(key=lambda x:(-x[1], x[0]))
    answer = [k[0] for k in fail_ratio]
    return answer