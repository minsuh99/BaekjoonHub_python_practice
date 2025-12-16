my_list = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            my_list[y + i][x + j] = 1

print(sum([sum(l) for l in my_list]))