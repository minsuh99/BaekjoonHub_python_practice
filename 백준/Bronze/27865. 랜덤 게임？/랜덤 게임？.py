import sys

N = int(sys.stdin.readline().strip())
while True:
    sys.stdout.write("? 1\n")
    sys.stdout.flush()
    
    temp = sys.stdin.readline().rstrip()
    if temp == 'Y':
        sys.stdout.write("! 1\n")
        sys.stdout.flush()
        break