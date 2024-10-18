import sys

T = int(sys.stdin.readline())

for i in range(T):
    num_list =[int(i) for i in sys.stdin.readline().split()]
    res = sum(num_list)
    print(f"Case #{i+1}: {num_list[0]} + {num_list[1]} = {res}")