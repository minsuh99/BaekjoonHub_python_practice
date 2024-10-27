import sys


N = int(sys.stdin.readline())

for _ in range(N):
    sentence = sys.stdin.readline().rstrip()
    for _ in range(len(sentence)):
        sentence = sentence.replace('()', '')
    
    if len(sentence) > 0:
        print("NO")
    else:
        print("YES")