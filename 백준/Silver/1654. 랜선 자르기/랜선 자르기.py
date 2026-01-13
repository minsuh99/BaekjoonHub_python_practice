import sys
input = sys.stdin.readline
# 만들려는 랜선의 길이가 커질 수록
# 그 랜선의 개수는 작아지고,
# 반대로 랜선 길이가 작아질 수록 랜선 개수가 많아짐
# 일관성 + 단조성이 있어 이분 탐색이 적절(하다는 생각을 떠올려야함)

K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))

lan.sort()

left = 1
right = max(lan)
mid = (left + right) // 2

while True:
    if left > right:
        break
    res = 0
    for l in lan:
        res += (l // mid)
    # 현재 랜선의 개수가 필요한 것보다 더 많기 때문에
    # mid 길이가 필요한 최대 길이보다 짧다는 것
    # left를 mid + 1로 이동
    if res >= N:
        left = mid + 1
    # 반대는 right를 mid - 1로 이동
    elif res < N:
        right = mid - 1
        
    mid = (left + right) // 2

print(right)