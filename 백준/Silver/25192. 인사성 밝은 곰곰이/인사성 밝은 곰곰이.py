import sys
input = sys.stdin.readline

N = int(input())
res = set()
cnt = 0 

for _ in range(N):
    str_ = input().rstrip()
    
    if str_ == "ENTER":
        cnt += len(res)
        res = set()
    else:
        res.add(str_)

if len(res) != 0:
    cnt += len(res)
    
print(cnt)