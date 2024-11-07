import sys

n, m = map(int, input().split())

password_dict = dict()

for _ in range(n):
    site, password = map(str, sys.stdin.readline().split())
    password_dict[site] = password

for _ in range(m):
    print(password_dict[str(sys.stdin.readline().strip())])