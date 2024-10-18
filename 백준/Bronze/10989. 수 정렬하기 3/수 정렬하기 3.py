import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for i in range(len(num_list)):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)


# 정렬 시 최댓값만큼의 counting list를 만든 후
# 인덱스가 해당 숫자, 리스트 요소 값은 해당 숫자가 나온 횟수
# 근데도 7828ms..
