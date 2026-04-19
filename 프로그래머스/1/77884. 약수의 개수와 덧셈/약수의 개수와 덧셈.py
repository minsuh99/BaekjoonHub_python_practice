def num_of_divisor(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:
                cnt += 1
            else:
                cnt += 2
    return cnt


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        temp = num_of_divisor(i)
        if temp % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer