def solution(record):
    answer = []
    res = []
    my_dict = dict()
    
    for rec in record:
        temp = rec.split()
        cmd = temp[0]
        uid = temp[1]
        if cmd == "Enter":
            name = temp[2]
            my_dict[uid] = name
            res.append([cmd, uid])
            
        elif cmd == "Change":
            name = temp[2]
            my_dict[uid] = name
            
        elif cmd == "Leave":
            res.append([cmd, uid])
    
    for r in res:
        if r[0] == "Enter":
            answer.append(f"{my_dict[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{my_dict[r[1]]}님이 나갔습니다.")
    
    return answer