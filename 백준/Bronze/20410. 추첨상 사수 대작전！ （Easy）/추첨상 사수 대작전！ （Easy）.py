import random

m, seed, x1, x2 = map(int, input().split())

while True:
    a = random.randint(0, m)
    c = random.randint(0, m)
    x1_temp = (a * seed + c) % m
    x2_temp = (a * x1_temp + c) % m
    if x1 == x1_temp and x2 == x2_temp:
        break
print(a, c)