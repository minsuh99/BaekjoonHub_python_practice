def solution(participant, completion):
    answer = ''
    
    participant_dict = {}
    
    for player in participant:
        if player not in participant_dict:
            participant_dict[player] = 1
        else:
            participant_dict[player] += 1
    
    for player in completion:
        participant_dict[player] -= 1
    
    final_idx = list(participant_dict.values()).index(1)
    answer = list(participant_dict.keys())[final_idx]
    return answer