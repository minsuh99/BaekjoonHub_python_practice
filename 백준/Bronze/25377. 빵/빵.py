n = int(input())
t_list = []
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        t_list.append(b)

print(min(t_list) if len(t_list) > 0 else -1)