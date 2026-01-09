import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    res = 0
    score = 0
    
    my_input = input().rstrip()
    for s in my_input:
        if s == "O":
            score += 1
        elif s == "X":
            score = 0
        res += score
    
    print(res)