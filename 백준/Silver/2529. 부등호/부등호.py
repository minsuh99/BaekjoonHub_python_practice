import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k = int(input())
inequal = input().split()

res_max = None
res_min = None

visited_max = [False for _ in range(10)]
visited_min = [False for _ in range(10)]

def valid(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b


def backtrack_max(res_list):
    global res_max

    if len(res_list) == k + 1:
        res_max = "".join(map(str, res_list))
        return True

    for cur_num in range(9, -1, -1):
        if visited_max[cur_num]:
            continue

        if len(res_list) == 0 or valid(res_list[-1], cur_num, inequal[len(res_list) - 1]):
            visited_max[cur_num] = True
            if backtrack_max(res_list + [cur_num]):
                return True
            visited_max[cur_num] = False

    return False


def backtrack_min(res_list):
    global res_min

    if len(res_list) == k + 1:
        res_min = "".join(map(str, res_list))
        return True

    for cur_num in range(10):
        if visited_min[cur_num]:
            continue

        if len(res_list) == 0 or valid(res_list[-1], cur_num, inequal[len(res_list) - 1]):
            visited_min[cur_num] = True
            if backtrack_min(res_list + [cur_num]):
                return True
            visited_min[cur_num] = False

    return False


backtrack_max([])
backtrack_min([])

print(res_max)
print(res_min)
