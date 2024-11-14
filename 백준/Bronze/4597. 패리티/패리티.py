import sys

while True:
    bit = sys.stdin.readline().strip()
    if bit == '#':
        break

    new_string = bit[:-1]
    parity = bit[-1]
    count_1 = new_string.count('1')
    
    if count_1 % 2 == 0 :
        if parity == 'e':
            print(new_string + '0')
        else:
            print(new_string + '1')
    else:
        if parity == 'e':
            print(new_string + '1')
        else:
            print(new_string + '0')
