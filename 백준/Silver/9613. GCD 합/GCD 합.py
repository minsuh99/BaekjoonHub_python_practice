import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

T = int(input())

for _ in range(T):
    my_list = [int(i) for i in input().split()[1:]]
    gcd_list = []
    
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            gcd_list.append(gcd(my_list[i], my_list[j]))
    
    print(sum(gcd_list))