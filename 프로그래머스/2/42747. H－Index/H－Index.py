def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h_index = citations[0]
    n = len(citations)
    while True:
        h_paper = len([c for c in citations if c >= h_index])
        if h_paper >= h_index and n - h_paper <= h_index:
            answer = h_index
            break
        
        h_index -= 1
    return answer