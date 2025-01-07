def solution(progresses, speeds):
    answer = []
    stack = []
    work_days = [0 for _ in range(len(progresses))]
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            work_days[i] = (100 - progresses[i]) // speeds[i]
        else:
            work_days[i] = (100 - progresses[i]) // speeds[i] + 1
    
    for day in work_days:
        if not stack or max(stack) >= day:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(day)
    answer.append(len(stack))
    return answer