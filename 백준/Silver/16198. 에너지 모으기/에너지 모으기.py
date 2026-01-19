import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
res = 0

def backtracking(energy, res_list):
    global res
    if len(res_list) == 2:
        res = max(res, energy)
        return
    
    temp = res_list.copy()
    
    for i in range(1, len(res_list) - 1):
        gain_energy = (res_list[i - 1] * res_list[i + 1])
        energy += gain_energy
        res_list = [res_list[j] for j in range(len(res_list)) if j != i]
        backtracking(energy, res_list)
        res_list = temp.copy()
        energy -= gain_energy

backtracking(0, num_list)
print(res)