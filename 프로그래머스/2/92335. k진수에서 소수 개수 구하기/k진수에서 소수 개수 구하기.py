import math

def solution(n, k):
    answer = -1
    
    def n_num(n, k):
        p = int(math.log(n, k))
        res = ''
        
        while n != 0:
            res += str(n // (k ** p))
            n %= k ** p
            p -= 1
        return res
    
    def is_prime(num):
        if num == 1:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num_list = [is_prime(int(i)) for i in n_num(n, k).split('0') if i != ""]
    
    answer = sum(num_list)
    return answer