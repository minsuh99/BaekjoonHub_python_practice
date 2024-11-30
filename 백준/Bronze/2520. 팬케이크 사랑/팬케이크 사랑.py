T = int(input())

for _ in range(T):
    _ = input()
    cm, y, ssu, ssa, f = map(int, input().split())
    b, gs, gc, w = map(int, input().split())
    
    dough = [int(i) for i in [cm / (8 / 16), y / (8 / 16), ssu / (4 / 16), ssa / (1 / 16), f / (9 / 16)]]
    cake = [int(i) for i in [b, gs / 30, gc / 25, w / 10]]

    print(min(min(dough), sum(cake)))