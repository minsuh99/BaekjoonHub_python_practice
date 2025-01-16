from itertools import combinations

def solution(orders, course):
    answer = []
    
    order_dict = {}
    
    for order in orders:
        temp = [s for s in order]
        for k in course:
            if len(temp) < k:
                continue
            else:
                for comb in list(combinations(temp, k)):
                    food = " ".join(comb).split()
                    food = "".join(sorted(comb))
                    if food in order_dict:
                        order_dict[food] += 1
                    else:
                        order_dict[food] = 1
                        
    print(order_dict)
    for k in course:
        try:
            most_order = max([value for key, value in order_dict.items() if (len(key) == k) and (value > 1)])
        except:
            continue
        best_food = [key for key, value in order_dict.items() if (len(key) == k) and (value == most_order)]
        print(most_order)
        answer.extend(best_food)
        answer.sort()
            
    return answer