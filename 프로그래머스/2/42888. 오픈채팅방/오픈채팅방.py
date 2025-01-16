def solution(record):
    answer = []
    new_records = []
    
    name_list = {}
    
    for rec in record:
        new_records.append(rec.split())
        if rec.split()[0] == "Leave":
            act, uid = map(str, rec.split())
        else:
            act, uid, nickname = map(str, rec.split())
            name_list[uid] = nickname
        
    
    for rec in new_records:
        uid = rec[1]
        if rec[0] == "Leave":
            message = f'{name_list[uid]}님이 나갔습니다.'
        elif rec[0] == 'Enter':
            message = f'{name_list[uid]}님이 들어왔습니다.'
        elif rec[0] == 'Change':
            continue
        answer.append(message)
    return answer

