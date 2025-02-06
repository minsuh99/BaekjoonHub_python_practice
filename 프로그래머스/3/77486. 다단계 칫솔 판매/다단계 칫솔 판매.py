def solution(enroll, referral, seller, amount):
    answer = []
    
    answer_dict = {}
    tree_dict = {}
    
    for enr in enroll:
        answer_dict[enr] = 0
        
    for enr, ref in zip(enroll, referral):
        if ref != "-":
            tree_dict[enr] = ref
    
    for sell, m in zip(seller, amount):
        cur = sell
        profit = m * 100
        
        while cur != "-" and profit > 0:
            answer_dict[cur] += (profit - (profit // 10))
            cur = tree_dict.get(cur, "-") # 수정
            profit //= 10
                
    answer = list(answer_dict.values())
    return answer