def solution(arr, divisor):
    answer = [i for i in sorted(arr) if i % divisor == 0]
    if not answer:
        answer = [-1]
    return answer