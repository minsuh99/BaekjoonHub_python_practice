import sys

cor_list=[]
N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    cor_list.append((a,b))

cor_list.sort(key=lambda x:x[1])
cor_list.sort(key=lambda x:x[0])

for i in range(N):
    print(cor_list[i][0], cor_list[i][1])