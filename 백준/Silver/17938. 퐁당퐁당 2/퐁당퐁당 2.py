N = int(input())
P, T = map(int, input().split())

arm_list = [int(i) for i in range(1, 2 * N+1)] * (3)
wheesoo_arm = [int(i) for i in range(2 * P - 1, 2 * P + 1)]
arm_num_list = [int(i) for i in range(1, 2 * N + 1)]
arm_num_list.extend([int(i) for i in range(2 * N - 1, 1, -1)])
arm_num = 0

for t in range(T - 1):
    arm_num += arm_num_list[t % len(arm_num_list)]

pos = arm_num % (2 * N)

final_arm_list = arm_list[pos:pos + arm_num_list[T % len(arm_num_list) - 1]]

res = 'Hing...NoJam'
for wheesoo in wheesoo_arm:
    if wheesoo in final_arm_list:
        res = "Dehet YeonJwaJe ^~^"
        break

print(res)