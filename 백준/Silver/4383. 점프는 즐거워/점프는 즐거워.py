import sys

while True:
    my_list = [int(i) for i in sys.stdin.readline().split()]
    if len(my_list) == 0:
        break
    
    n = my_list[0]
    my_list = my_list[1:]
    gt = [i for i in range(1, n)]
    
    check_list = [abs(my_list[i - 1] - my_list[i]) for i in range(1, len(my_list))]
    
    if list(set(check_list)) == gt:
        print("Jolly")
    else:
        print("Not jolly")
    