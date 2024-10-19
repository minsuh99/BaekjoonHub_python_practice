import sys

n = int(sys.stdin.readline())
n_list = set([int(i) for i in sys.stdin.readline().split()]) # set으로 저장하면 탐색 시간이 줄어듬 / list와의 차이
m = int(sys.stdin.readline())
m_list = [int(i) for i in sys.stdin.readline().split()]

for i in range(m):
    print(1) if m_list[i] in n_list else print(0)

# 시간 초과,,
# set vs list