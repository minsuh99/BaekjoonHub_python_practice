import sys

n = int(sys.stdin.readline())

my_list = [0 for _ in range(n + 1)]
score = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(score[0])
    sys.exit()
if n == 2:
    print(score[0] + score[1])
    sys.exit()

my_list[0] = score[0]
my_list[1] = score[0] + score[1]
my_list[2] = max(my_list[0] + score[2], score[1] + score[2])

for i in range(3, n):
    my_list[i] = max(my_list[i-2] + score[i], my_list[i-3] + score[i-1] + score[i])

print(my_list[n-1])