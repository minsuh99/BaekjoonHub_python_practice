my_list = [[i for i in input().rstrip()[::-1]] for _ in range(5)]
res = []
max_len = max([len(l) for l in my_list])

for _ in range(max_len):
    for i in range(5):
        if my_list[i]:
            res.append(my_list[i].pop())

print("".join(res))