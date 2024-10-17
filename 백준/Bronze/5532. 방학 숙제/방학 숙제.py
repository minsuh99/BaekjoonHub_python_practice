import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

max_study_day = 0

print(l - max(math.ceil(a/c),math.ceil(b/d)))
