import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_listen = set()
not_seen = set()

for _ in range(N):
    not_listen.add(input().rstrip())

for _ in range(M):
    not_seen.add(input().rstrip())

res = sorted(list(not_listen & not_seen))
print(len(res))
for name in res:
    print(name)