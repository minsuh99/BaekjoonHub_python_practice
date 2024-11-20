import sys


cnt = 1
while True:
    inp = sys.stdin.readline().strip()
    if inp == '0':
        break
    else:
        print(f"Case {cnt}: Sorting... done!")
        cnt += 1