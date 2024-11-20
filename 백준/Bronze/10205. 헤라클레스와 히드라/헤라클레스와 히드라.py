import sys
input = sys.stdin.readline

lst = []
n = int(input())

for i in range(1, n+1):
    h = int(input())
    a = input().rstrip()
    for j in a:
        if h == 0:
            break
        if j == 'b':
            h -= 1
        elif j == 'c':
            h += 1
    lst.append(h)
for k in range(len(lst)):
    print("Data Set %d:" %  int(k+1))
    print(lst[k])
    print("\n", end="")