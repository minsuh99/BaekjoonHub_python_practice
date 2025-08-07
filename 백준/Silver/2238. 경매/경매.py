from collections import defaultdict
import sys
input = sys.stdin.readline

U, N = map(int, input().rstrip().split())

my_dict = defaultdict(list)

for _ in range(N):
    name, price = map(str, input().rstrip().split())
    my_dict[int(price)].append(name)

my_dict = sorted(my_dict.items(), key=lambda x: (len(x[1]), x[0]))

print(my_dict[0][1][0], my_dict[0][0])
