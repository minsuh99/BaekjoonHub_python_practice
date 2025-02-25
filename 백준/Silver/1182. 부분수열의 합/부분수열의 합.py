import sys

n, s = map(int, sys.stdin.readline().split())
my_list = [int(i) for i in sys.stdin.readline().split()]
res = 0
def backtrack(k, start, comb_list):
    global res
    if len(comb_list) == k:
        if sum(comb_list) == s:
            res += 1
            return
    
    for i in range(start, n):
        comb_list.append(my_list[i])
        backtrack(k, i + 1, comb_list)
        comb_list.pop()
    
for k in range(1, n+1):
    backtrack(k, 0, [])

print(res)