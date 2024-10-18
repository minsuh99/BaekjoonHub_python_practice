from math import ceil

a, b, v = map(int, input().split())

day = ceil((v-a) / (a-b))
print(day+1)