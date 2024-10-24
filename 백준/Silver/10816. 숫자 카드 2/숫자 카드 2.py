import sys

n = int(sys.stdin.readline())
card_list = [int(i) for i in sys.stdin.readline().split()]

m = int(sys.stdin.readline())
num_list = [int(i) for i in sys.stdin.readline().split()]

res_dict = {}

for i in card_list:
    if i in res_dict:
        res_dict[i] += 1
    else:
        res_dict[i] = 1

for num in num_list:
    print(res_dict[num] if num in res_dict else 0, end = " ")

# 딕셔너리가 시간 줄이는데 좀 도움이 되나봄
# 리스트의 count 메소드는 O(n)이기에 리스트 요소마다 반복문을 실행하면
# O(n^2)이라 시간 오래 걸리나봄
