def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    clothes = [1 for _ in range(n + 2)]
    
    for student in lost:
        clothes[student] -= 1
    
    for student in reserve:
        clothes[student] += 1
    
    borrow_student = [s for s in lost if s not in reserve]
    for student in borrow_student:
        if clothes[student - 1] == 2:
            clothes[student - 1] -= 1
            clothes[student] += 1
            continue
        elif clothes[student + 1] == 2:
            clothes[student + 1] -= 1
            clothes[student] += 1
            continue
    
    print(clothes[1:-1])
    answer = n - len([i for i in clothes if i == 0])
    return answer