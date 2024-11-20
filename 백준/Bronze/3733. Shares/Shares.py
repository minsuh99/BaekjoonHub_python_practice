import sys

while True:
    inp = sys.stdin.readline().strip()
    if inp == '':
        break
    n, s = map(int, inp.split())
    print(s // (n + 1))