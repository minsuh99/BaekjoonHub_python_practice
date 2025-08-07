def gcd(a, b):
    if a == 0 or b == 0:
        return a if b == 0 else b
    (a, b) = (b, a) if b > a else (a, b)
    return gcd(a % b, b)

s = input()
t = input()

len_s = len(s)
len_t = len(t)

lcm = len_s * len_t // gcd(len_s, len_t)

f_s = s * (lcm // len_s)
f_t = t * (lcm // len_t)

if f_s == f_t:
    print(1)
else:
    print(0)