def solution(citations):
    answer = 0
    citations.sort()
    temp = []
    h_index = citations[-1]
    
    for h in range(h_index, 0, -1):
        while True:
            if citations and citations[-1] >= h:
                temp.append(citations.pop())
            else:
                break
                
        if len(temp) >= h and len(citations) <= h:
            return h

    return answer