from itertools import combinations


def solution(nums):
    answer = 0
    max_num = max(nums) * 3
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    
    for comb in list(combinations(nums, 3)):
        if is_prime[sum(comb)]:
            answer += 1

    return answer