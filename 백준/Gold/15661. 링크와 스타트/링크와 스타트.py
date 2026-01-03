import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

W = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        W[i][j] = S[i][j] + S[j][i]

players = list(range(N))
ans = 10**6

def team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += W[team[i]][team[j]]
    return score

for k in range(1, N//2 + 1):
    for teamA in combinations(players, k):
        teamA = set(teamA)
        teamB = [p for p in players if p not in teamA]

        scoreA = team_score(list(teamA))
        scoreB = team_score(teamB)

        ans = min(ans, abs(scoreA - scoreB))

print(ans)
