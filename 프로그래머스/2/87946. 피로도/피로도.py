from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for permutation in list(permutations(dungeons, len(dungeons))):
        cur_k = k
        count = 0
        
        for i in range(len(permutation)):
            if cur_k >= permutation[i][0] and cur_k - permutation[i][1] >= 0:
                cur_k -= permutation[i][1]
                count += 1
            else:
                break
        
        if count == len(dungeons):
            return len(dungeons)
        
        if count > answer:
            answer = count
    return answer