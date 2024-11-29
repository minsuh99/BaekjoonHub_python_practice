num_list = []

n = int(input())

for _ in range(n):
    s, a = map(int, input().split())
    num_list.append(a % s)

print(sum(num_list))