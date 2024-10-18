import sys

while True:
    num = input()
    if num == '0': break
    num2 = num[::-1]
    if num == num2:
        print('yes')
    else:
        print('no')