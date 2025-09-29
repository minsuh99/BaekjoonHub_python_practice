import sys
input = sys.stdin.readline

S, P = map(int, input().split())
my_str = list(input().rstrip())
check_dict = dict()
check_dict['A'], check_dict['C'], check_dict['G'], check_dict['T'] = map(int, input().split())
my_dict = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

start_idx = 0
end_idx = start_idx + (P - 1)
cnt = 0

for i in range(start_idx, end_idx + 1):
    my_dict[my_str[i]] += 1

while True:
    if my_dict['A'] >= check_dict['A'] and my_dict['C'] >= check_dict['C'] and my_dict['G'] >= check_dict['G'] and my_dict['T'] >= check_dict['T']:
        cnt += 1
    
    if end_idx == S - 1:
        break
    else:
        my_dict[my_str[start_idx]] -= 1
        start_idx += 1
        end_idx += 1
        my_dict[my_str[end_idx]] += 1

print(cnt)