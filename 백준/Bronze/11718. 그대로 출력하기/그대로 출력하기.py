import sys
my_list = []
while True:
    s = sys.stdin.readline().rstrip()
    if s != "":
        my_list.append(s)
    else:
        break

for strs in my_list:
    print(strs)

# try, except 구문도 괜찮네
