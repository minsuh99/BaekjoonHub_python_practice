from collections import Counter


def solution(k, tangerine):
    answer = 0
    my_dict = Counter(tangerine)
    num_kind = sorted([v for _, v in my_dict.items()], reverse=True)
    cur_k = 0
    
    for i in range(len(num_kind)):
        answer += 1
        cur_k += num_kind[i]
        if cur_k >= k:
            break
    return answer