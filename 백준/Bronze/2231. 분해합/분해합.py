# def decompose_sum(n: int):
#     return n + sum([int(i) for i in str(n)])
    

# n = int(input())
# res = 0
# for i in range(n):
#     if decompose_sum(i) == n:
#         res = i
#         break
# print(res)

# 브루트포스 알고리즘
# 1176ms

# n = int(input())
# res = 0
# for i in range(1, n+1):
#     decompose_sum = i + sum(map(int, str(i)))
#     if decompose_sum == n:
#         res = i
#         break

# print(res)

# 1104 ms

n = int(input())
res = 0

for i in range(max(1, n-9*len(str(n))), n):
    decompose_sum = i + sum(map(int, str(i)))
    if decompose_sum == n:
        res = i
        break

print(res)

# 32ms
# 탐색 시작점을 잘 찾으면 다 탐색할 필요 없다..
# 3자리 정수이면 3자리 정수의 자릿수 합 최댓값을 빼면 시작점이 될것이다..
