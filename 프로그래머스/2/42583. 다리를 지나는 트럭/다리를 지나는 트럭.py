from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    truck_weights = deque(truck_weights)
    cur_time = 0
    cur_weight = 0
    while bridge or truck_weights:
        cur_time += 1
        
        if bridge:
            if bridge[0][0] + bridge_length == cur_time:
                cur_weight -= bridge[0][1]
                bridge.popleft()
                
        if truck_weights:
            if cur_weight + truck_weights[0] <= weight and len(bridge) <= bridge_length:
                cur_weight += truck_weights[0]
                bridge.append((cur_time, truck_weights.popleft()))
    
    answer = cur_time
    return answer