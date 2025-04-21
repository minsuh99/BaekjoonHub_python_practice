n, m = map(int, input().split())
my_dict = dict()
for _ in range(n):
    word = input()
    my_dict[word] = 0

for _ in range(m):
    w = input()
    if w in my_dict:
        my_dict[w] += 1

print(sum(list(my_dict.values())))