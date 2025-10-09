import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    parking_fee = defaultdict(list)
    
    for record in records:
        time, car_num, status = record.split()
        hour, minute = time.split(":")
        cur_time = int(hour) * 60 + int(minute)
        parking_fee[car_num].append(cur_time)
        
    for car_num, time_record in sorted(parking_fee.items()):
        temp = 0
        if len(time_record) % 2 != 0:
            time_record.append(60*23+59)
        for j in range(0, len(time_record), 2):
            temp += time_record[j + 1] - time_record[j]
        
        if temp <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((temp - fees[0]) / fees[2]) * fees[3])

        
    return answer