N = int(input())
res = 0
cur_digit = len(str(N))
if cur_digit == 1:
    print(N)
    exit()

temp = 9

for i in range(cur_digit - 1):
    res += temp * (i + 1)
    temp *= 10

cur_digit_min = 10 ** (cur_digit - 1)
res += cur_digit * (N - cur_digit_min + 1)
print(res)