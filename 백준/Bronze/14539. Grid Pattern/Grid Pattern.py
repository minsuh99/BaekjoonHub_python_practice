def draw_horizon(w, col):
    print("+", end='')
    for _ in range(col):
        print("-" * w, end='')
        print("+", end='')
    print()

def draw_star_line(w, h, col):
    for _ in range(h):
        print("|", end='')
        for _ in range(col):
            print("*" * w, end='')
            print("|", end='')
        print()
            


T = int(input())

for t in range(T):
    row, col, w, h = map(int, input().split())
    
    print(f'Case #{t+1}:')
    
    for _ in range(row):
        draw_horizon(w, col)
        draw_star_line(w, h, col)
    draw_horizon(w, col)