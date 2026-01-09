L = int(input())
my_str = input()
res = 0

for i in range(L):
    res += (ord(my_str[i]) - ord('a') + 1) * (31 ** i)

print(res % 1234567891)