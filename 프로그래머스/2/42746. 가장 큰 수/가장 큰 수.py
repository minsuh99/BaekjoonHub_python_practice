def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x:x*4, reverse=True)
    answer = "".join(numbers) if sum([int(i) for i in numbers]) != 0 else '0'
    return answer