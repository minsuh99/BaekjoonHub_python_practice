from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = []
    for length in range(1, len(numbers) + 1):
        for num_str in list(set((permutations(numbers, length)))):
            temp = int("".join(num_str))
            if temp not in num_list:
                num_list.append(temp)

    answer = sum([is_prime(num) for num in num_list])
    return answer