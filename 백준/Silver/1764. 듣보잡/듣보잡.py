import sys
n, m = map(int, sys.stdin.readline().split())
non_listen = set()
non_watch = set()

for _ in range(n):
    non_listen.add(sys.stdin.readline().strip())

for _ in range(m):
    non_watch.add(sys.stdin.readline().strip())

res_list = sorted(list(non_listen.intersection(non_watch)))
print(len(res_list))
for name in res_list:
    print(name)