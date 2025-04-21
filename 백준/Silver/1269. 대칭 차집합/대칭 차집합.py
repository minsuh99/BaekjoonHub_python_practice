a, b = map(int, input().split())
set_a = set([int(i) for i in input().split()])
set_b = set([int(i) for i in input().split()])

res = set_a ^ set_b

print(len(res))
