def solution(d, budget):
    answer = 0
    d.sort()
    price = 0
    for p in d:
        if price + p > budget:
            break
        price += p
        answer += 1
        
    return answer