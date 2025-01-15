def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    
    for product in want:
        if product not in discount:
            return 0
    
    for product, num in zip(want, number):
        want_dict[product] = num
    
    for i in range(len(discount) - 9):
        check_products = discount[i:i+10]
        check_dict = {}
        
        for product in check_products:
            if product not in check_dict:
                check_dict[product] = 1
            else:
                check_dict[product] += 1
    
        answer += (want_dict == check_dict)
    
    return answer