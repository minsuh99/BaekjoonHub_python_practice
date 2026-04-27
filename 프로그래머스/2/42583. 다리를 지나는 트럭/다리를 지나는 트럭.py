from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge_truck = deque([])
    cur_weight = 0
    
    while trucks or bridge_truck:
        answer += 1
        if bridge_truck and answer - bridge_truck[0][0] == bridge_length:
            _, w = bridge_truck.popleft()
            cur_weight -= w
        
        if trucks and cur_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            cur_weight += truck
            bridge_truck.append((answer, truck))

    return answer