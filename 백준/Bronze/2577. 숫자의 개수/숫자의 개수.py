a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)

for n in range(10):
    print(num.count(str(n)))
