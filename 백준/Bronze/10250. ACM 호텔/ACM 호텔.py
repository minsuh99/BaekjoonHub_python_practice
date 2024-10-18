T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    print(f"{n%h if n%h!=0 else h}{n//h+1 if n%h != 0 else n//h:02d}")