T = int(input())

for test_case in range(1, T + 1):
    res = 100001
    arr = [int(i) for i in input().split()]
    N = arr[0]
    arr = arr[1:]
    
    
    def dfs(idx, battery, cnt):
        global res

        if cnt >= res:
            return

        if idx == N - 1:
            res = min(res, cnt)
            return

        if battery > 0:
            dfs(idx + 1, battery - 1, cnt)

        if idx < N - 1:
       		dfs(idx + 1, arr[idx] - 1, cnt + 1)
    
    dfs(1, arr[0] - 1, 0)
    
    print(f"#{test_case} {res}")