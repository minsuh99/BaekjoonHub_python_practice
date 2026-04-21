def solution(n, lost, reserve):
    answer = 0
    have_cloth = [True if i + 1 not in lost else False for i in range(n)]
    reserve_cloth = [True if i + 1 in reserve else False for i in range(n)]
    
    for i in range(n):
        if not have_cloth[i] and reserve_cloth[i]:
            have_cloth[i] = True
            reserve_cloth[i] = False
    
    for i in range(n):
        if not have_cloth[i]:
            if reserve_cloth[i]:
                have_cloth[i] = True
                reserve_cloth[i] = False
                continue
            elif i > 0 and reserve_cloth[i - 1]:
                have_cloth[i] = True
                reserve_cloth[i - 1] = False
                continue
            elif i < n - 1 and reserve_cloth[i + 1]:
                have_cloth[i] = True
                reserve_cloth[i + 1] = False
                continue
    
    return sum(have_cloth)