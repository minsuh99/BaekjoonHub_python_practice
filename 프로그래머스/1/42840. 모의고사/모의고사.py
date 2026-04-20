def solution(answers):
    res = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0, 0]
    
    for i, answer in enumerate(answers):
        if num1[i % 5] == answer:
            correct[1] += 1
        if num2[i % 8] == answer:
            correct[2] += 1
        if num3[i % 10] == answer:
            correct[3] += 1
    
    max_cor = max(correct)
    for i in range(1, 4):
        if correct[i] == max_cor:
            res.append(i)
    return res