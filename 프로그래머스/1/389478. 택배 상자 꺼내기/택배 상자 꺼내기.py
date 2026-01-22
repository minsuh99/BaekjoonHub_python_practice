def solution(n, w, num):
    answer = 0
    w_array = [0 for _ in range(w)]
    
    for i in range(1, n + 1):
        r = (i - 1) // w
        if r % 2 == 0:
            c = (i - 1) % w
        else:
            c = w - 1 - (i - 1) % w
        w_array[c] += 1
    
        if i == num:
            target_r, target_c = r, c
    
    answer = w_array[target_c] - target_r
            
    return answer