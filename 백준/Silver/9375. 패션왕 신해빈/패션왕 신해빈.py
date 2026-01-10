from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(0)
        continue
    
    cloth_dict = defaultdict(list)
    res = 1
    for _ in range(N):
        cloth, kind = map(str, input().rstrip().split())
        if cloth_dict[kind]:
            cloth_dict[kind].append(cloth)
        else:
            cloth_dict[kind] = [cloth]
    
    for key in cloth_dict.keys():
        res *= len(cloth_dict[key]) + 1
    
    print(res - 1)