"""
025 친구 관계 파악하기 (백준 13023, 골드 5)
시간제한 2초

문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 
사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 
A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 
친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

예제 입력 1 
5 4
0 1
1 2
2 3
3 4
예제 출력 1 
1
예제 입력 2 
5 5
0 1
1 2
2 3
3 0
1 4
예제 출력 2 
1
예제 입력 3 
6 5
0 1
0 2
0 3
0 4
0 5
예제 출력 3 
0
예제 입력 4 
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
예제 출력 4 
1
"""

## DFS를 활용해서 깊이를 탐색할 때, 그 깊이가 5인게 같다면..?

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
res = 0

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(graph, start, visited, depth):
    global res
    cur_depth = depth
    if cur_depth == 5:
        res = 1
        return
    visited[start] = True
    
    for node in graph[start]:
        if visited[node] == False:
            cur_depth += 1
            dfs(graph, node, visited, cur_depth)
            cur_depth -= 1
    visited[start] = False

for node in range(N):
    if visited[node] == False:
        dfs(graph, node, visited, 1)
        if res == 1:
            break

print(res)