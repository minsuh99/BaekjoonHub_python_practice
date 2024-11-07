socks = [0] * 10
for _ in range(5):
    socks[int(input())] += 1

for i in socks:
    if i % 2 != 0:
        print(socks.index(i))