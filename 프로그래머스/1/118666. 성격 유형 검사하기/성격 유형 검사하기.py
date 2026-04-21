def solution(survey, choices):
    answer = ''
    index_ = ["RT", "CF", "JM", "AN"]
    index_score = [{k:0 for k in idx} for idx in index_]
    
    for i, choice in enumerate(choices):
        if choice == 4:
            continue
        
        if survey[i] in index_:
            idx = index_.index(survey[i])
        else:
            idx = index_.index(survey[i][::-1])
            
        if choice > 4:
            index_score[idx][survey[i][1]] += abs(choice - 4)
        
        elif choice < 4:
            index_score[idx][survey[i][0]] += abs(choice - 4)
    
    answer = "".join([max(d, key=d.get) for d in index_score])
    return answer