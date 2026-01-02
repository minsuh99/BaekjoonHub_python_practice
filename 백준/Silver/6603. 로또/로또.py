import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

while True:
    my_input = input().rstrip()
    if my_input == '0':
        exit()
    
    temp = [int(i) for i in my_input.split()]
    k = temp[0]
    num_list = temp[1:]
    
    def backtrack(start, res_list):
        if len(res_list) == 6:
            print(*res_list)
            return
        
        for i in range(start, k):
            res_list.append(num_list[i])
            backtrack(i + 1, res_list)
            res_list.pop()

    backtrack(0, [])
    print()