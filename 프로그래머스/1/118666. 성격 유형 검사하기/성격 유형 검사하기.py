def solution(survey, choices):
    answer = ''
    index_ = ["RT", "CF", "JM", "AN"]
    index_score = [{k: 0 for k in idx} for idx in index_]

    for pair, choice in zip(survey, choices):
        if choice == 4:
            continue

        for i, idx in enumerate(index_):
            if pair[0] in idx and pair[1] in idx:
                if choice < 4:
                    index_score[i][pair[0]] += 4 - choice
                else:
                    index_score[i][pair[1]] += choice - 4
                break

    for pair, d in zip(index_, index_score):
        if d[pair[0]] >= d[pair[1]]:
            answer += pair[0]
        else:
            answer += pair[1]

    return answer