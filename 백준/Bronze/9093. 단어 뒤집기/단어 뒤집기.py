T = int(input())

for _ in range(T):
    my_list = [i[::-1] for i in input().split()]
    print(" ".join(my_list))