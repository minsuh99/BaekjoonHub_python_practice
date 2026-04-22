def solution(elements):
    answer = set()
    circle = elements + elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(circle[i:i+j]))
    return len(answer)