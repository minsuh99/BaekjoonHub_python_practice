import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
    
visited = [False for _ in range(N)]
res = 10 ** 6


def backtrack(start, res_list):
    global res
    
    if len(res_list) == N // 2:
        team1 = res_list.copy()
        team2 = [int(i) for i in range(N) if i not in team1]
        
        stat1 = 0
        stat2 = 0
        
        for i in range(N - 1):
            for j in range(i + 1, N // 2):
                stat1 += S[team1[i]][team1[j]]
                stat1 += S[team1[j]][team1[i]]
                
                stat2 += S[team2[i]][team2[j]]
                stat2 += S[team2[j]][team2[i]]

        res = min(res, abs(stat1 - stat2))
        return
    
    for i in range(start, N):
        if visited[i]:
            continue
        
        visited[i] = True
        res_list.append(i)
        backtrack(i + 1, res_list)
        res_list.pop()
        visited[i] = False

backtrack(0, [])
print(res)