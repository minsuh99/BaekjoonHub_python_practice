n = int(input())

for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    a_, b_, c_ = sorted(map(int, input().split()))
    
    if (a, b, c) == (a_, b_, c_) and a*a + b*b == c*c:
        print("YES")
    else:
        print("NO")