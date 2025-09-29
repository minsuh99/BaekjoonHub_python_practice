N = int(input())
start_idx = 1
end_idx = 1
temp_sum = 1
cnt = 1 # 자기 자신은 무조건 있어서 그런가?

while end_idx != N:
    if temp_sum == N:
        cnt += 1
        end_idx += 1
        temp_sum += end_idx
    elif temp_sum > N:
        temp_sum -= start_idx
        start_idx += 1
    else:
        end_idx += 1
        temp_sum += end_idx
print(cnt)