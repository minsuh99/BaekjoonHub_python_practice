def solution(k, score):
    answer = []
    hof = []

    for s in score:
        if len(hof) < k:
            hof.append(s)
        else:
            m = min(hof)
            if s > m:
                hof[hof.index(m)] = s

        answer.append(min(hof))

    return answer