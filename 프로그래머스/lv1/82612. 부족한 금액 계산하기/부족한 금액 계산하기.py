def solution(price, money, count):
    need_money = price * (count * (count + 1) // 2)
    answer = need_money - money if need_money > money else 0
    return answer