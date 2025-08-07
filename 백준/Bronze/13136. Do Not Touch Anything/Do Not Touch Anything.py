R, C, N = map(int, input().split())

def get_num(num1, num2):
    if num1 % num2 != 0:
        return num1 // num2 + 1
    else:
        return num1 // num2

print(get_num(R, N) * get_num(C, N))