import sys

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a < b:
            big, small = b, a
        else:
            big, small = a, b
    
        return gcd(big%small, small)

input = sys.stdin.readline

N = int(input())
my_list = []
for _ in range(N):
    my_list.append(int(input()))

diff_list = [my_list[i + 1] - my_list[i] for i in range(N - 1)]
final_gcd = 0

final_gcd = gcd(diff_list[0], diff_list[1])
if len(diff_list) != 2:
    for num in diff_list[2:]:
        final_gcd = gcd(final_gcd, num)

print(len(range(my_list[0], my_list[-1] + 1, final_gcd)) - len(my_list))