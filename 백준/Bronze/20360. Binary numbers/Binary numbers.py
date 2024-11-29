n = int(input())

num_list = []
for p in range(19, -1, -1):
    if n >= 2 ** p:
        n -= 2 ** p
        num_list.append(p)
num_list = [str(i) for i in sorted(num_list)]

print(" ".join(num_list))