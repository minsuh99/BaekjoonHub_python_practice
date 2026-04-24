from collections import deque


def solution(progresses, speeds):
    answer = []
    progress_queue = deque(progresses)
    speed_queue = deque(speeds)
    stack = []
    
    while progress_queue:
        for i in range(len(progress_queue)):
            progress_queue[i] += speed_queue[i]
        if progress_queue[0] >= 100:
            while progress_queue and progress_queue[0] >= 100:
                stack.append(progress_queue.popleft())
                speed_queue.popleft()
            answer.append(len(stack))
            stack = []
    
    return answer