while True:
    my_num = input()
    if my_num == "0":
        exit()
    
    if my_num == my_num[::-1]:
        print("yes")
    else:
        print("no")