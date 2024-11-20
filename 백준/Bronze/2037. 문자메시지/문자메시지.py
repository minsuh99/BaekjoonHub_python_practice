def calc_time(alphabet, push, wait):  
    for pad in keypad:
        if alphabet in pad:
            idx = pad.index(alphabet)
            return push * (idx + 1) + wait * (idx)
        


p, w = map(int, input().split())
sentence = [i for i in input()]

time = 0
keypad = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
pad_num = 1

for alphabet in sentence:
    if alphabet == ' ':
        pad_num = 1
        time += p
        continue
    else:
        for pad in keypad:
            if alphabet in pad:
                check_num = keypad.index(pad) + 2
                push_num = pad.index(alphabet) + 1
                break
        if check_num == pad_num:
            time += w
        pad_num = check_num
        time += p * push_num
            
print(time)