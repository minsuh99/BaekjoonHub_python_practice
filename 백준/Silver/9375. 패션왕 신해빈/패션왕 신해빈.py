from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    my_dict = defaultdict(list)
    answer = 1
    
    t = int(input())
    for _ in range(t):
        wear, kind = map(str, input().split())
        if kind not in my_dict:
            my_dict[kind] = [wear]
        else:
            my_dict[kind].append(wear)
        
    for key in my_dict.keys():
        answer *= len(my_dict[key]) + 1

    answer -= 1
    print(answer)