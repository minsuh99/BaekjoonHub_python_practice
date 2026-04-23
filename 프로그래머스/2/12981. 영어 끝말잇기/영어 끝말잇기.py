def solution(n, words):
    player_num = 0
    order_num = 0
    stack = []
    
    for i, word in enumerate(words):
        if (stack and stack[-1][-1] != word[0]) or word in stack:
            player_num = i % n + 1
            order_num = i // n + 1
            break
        else:
            stack.append(word)
            
    return [player_num, order_num]