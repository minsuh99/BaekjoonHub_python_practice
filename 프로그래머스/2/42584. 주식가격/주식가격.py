def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i, price in enumerate(prices):
        if stack:
            for t in stack:
                answer[t[0]] += 1
            
        if stack and stack[-1][1] > price:
            while stack and stack[-1][1] > price:
                stack.pop()

        stack.append((i, price))    

    return answer