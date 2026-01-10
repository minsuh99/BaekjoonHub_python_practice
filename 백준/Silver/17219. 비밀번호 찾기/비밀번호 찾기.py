import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pass_dict = {}

for _ in range(N):
    site, password = map(str, input().rstrip().split())
    pass_dict[site] = password

for _ in range(M):
    find_site = input().rstrip()
    print(pass_dict[find_site])
