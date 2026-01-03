import sys
input = sys.stdin.readline

S = [0 for _ in range(21)]
M = int(input())

for _ in range(M):
    oper = input().rstrip().split()
    if oper[0] == "add" and S[int(oper[1])] == 0:
        S[int(oper[1])] = 1
    if oper[0] == "remove" and S[int(oper[1])] == 1:
        S[int(oper[1])] = 0
    if oper[0] == "check":
        print(1 if S[int(oper[1])] == 1 else 0)
    if oper[0] == "toggle":
        if S[int(oper[1])] == 0:
            S[int(oper[1])] = 1
        else:
            S[int(oper[1])] = 0
    if oper[0] == "all":
        S = [1] * 21
    if oper[0] == "empty":
        S = [0] * 21