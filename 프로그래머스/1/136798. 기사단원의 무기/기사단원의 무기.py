def num_of_divisor(n):
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:
                res += 1
            else:
                res += 2
    return res


def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        temp = num_of_divisor(num)
        if temp <= limit:
            answer += temp
        else:
            answer += power
    return answer