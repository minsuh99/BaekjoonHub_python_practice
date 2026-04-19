def solution(k, score):
    answer = []
    hof = []
    for s in score:
        if not hof:
            hof.append(s)
            answer.append(s)
        else:
            hof.sort()
            if len(hof) == k:
                if s > min(hof):
                    hof.append(s)
                    hof.remove(min(hof))
            else:
                hof.append(s)
            answer.append(min(hof))

    return answer