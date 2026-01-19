import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

max_val = -10 ** 9
min_val = 10 ** 9

def backtrack(idx, cur_res):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, cur_res)
        min_val = min(min_val, cur_res)
        return
    
    for i in range(4):
        if oper_list[i] > 0:
            oper_list[i] -= 1
            if i == 0:
                backtrack(idx + 1, cur_res + num_list[idx])
            elif i == 1:
                backtrack(idx + 1, cur_res - num_list[idx])
            elif i == 2:
                backtrack(idx + 1, cur_res * num_list[idx])
            elif i == 3:
                if cur_res < 0:
                    backtrack(idx + 1, (abs(cur_res) // num_list[idx]) * -1)
                else:
                    backtrack(idx + 1, abs(cur_res) // num_list[idx])
            oper_list[i] += 1

backtrack(1, num_list[0])
print(max_val)
print(min_val)