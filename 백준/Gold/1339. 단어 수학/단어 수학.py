from collections import defaultdict
import sys
input = sys.stdin.readline

my_dict = defaultdict(int)
res = 0
num = 9

N = int(input())
for _ in range(N):
    word = input().rstrip()
    for i in range(len(word)):
        my_dict[word[i]] += 10 ** (len(word) - i - 1)


for _, v in sorted(my_dict.items(), key=lambda x: -x[1]):
    res += v * num
    num -= 1

print(res)