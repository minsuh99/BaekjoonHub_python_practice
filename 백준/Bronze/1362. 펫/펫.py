import sys

o = 0
w = 0
scenario = 1
while True:
    input1, input2 = map(str, sys.stdin.readline().split())

    if input1 == '0' and input2 == '0':
        break
    
    if o == 0 & w == 0:
        o = int(input1)
        w = int(input2)
    if input1 == "#" and input2 == '0':

        if w > o * 0.5 and w < o * 2:
            print(f'{scenario} :-)')
        elif w <= 0:
            print(f'{scenario} RIP')
        else:
            print(f'{scenario} :-(')
        
        o = 0
        w = 0
        scenario += 1
    else:
        if input1 == "E":
            if w <= 0:
                pass
            else:
                w -= int(input2)
        elif input1 == "F":
            if w <= 0:
                pass
            else:
                w += int(input2)
    