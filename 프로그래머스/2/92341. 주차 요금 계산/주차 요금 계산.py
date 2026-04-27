def solution(fees, records):
    answer = []
    res_dict = dict()
    parking_dict = dict()
    
    for record in records:
        t, car, rec = record.split()
        h, m = map(int, t.split(":"))
        
        if rec == "IN":
            parking_dict[car] = h * 60 + m
        
        elif rec == "OUT":
            if car not in res_dict:
                res_dict[car] = h * 60 + m - parking_dict[car]
            else:
                res_dict[car] += h * 60 + m - parking_dict[car]
            
            del parking_dict[car]

    if parking_dict:
        for car in parking_dict.keys():
            if car not in res_dict:
                res_dict[car] = 23 * 60 + 59 - parking_dict[car]
            else:
                res_dict[car] += 23 * 60 + 59 - parking_dict[car]
    
    res_dict = dict(sorted(res_dict.items(), key = lambda x:x[0]))
    
    for v in res_dict.values():
        if v <= fees[0]:
            answer.append(fees[1])
        else:
            res = fees[1] + (((v - fees[0]) + fees[2] - 1) // fees[2]) * fees[3]
            answer.append(res)
    return answer