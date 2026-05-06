def solution(storey):
    answer = 0
    
    while storey != 0:
        check_digit = storey % 10
        if 1 <= check_digit < 5:
            answer += check_digit
            storey -= check_digit
        elif check_digit == 5:
            next_digit = (storey // 10) % 10
            if next_digit < 5:
                answer += check_digit
                storey -= check_digit
            else:
                answer += 10 - check_digit
                storey += 10 - check_digit
        elif 6 <= check_digit <= 9:
            answer += 10 - check_digit
            storey += 10 - check_digit
        storey //= 10
    return answer