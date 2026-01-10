import sys
input = sys.stdin.readline

fibo_res = [_ for _ in range(41)]
fibo_res[0] = (1, 0)
fibo_res[1] = (0, 1)
for i in range(2, 41):
    zero = fibo_res[i - 1][0] + fibo_res[i - 2][0]
    one = fibo_res[i - 1][1] + fibo_res[i - 2][1]
    fibo_res[i] = (zero, one)

T = int(input())
for _ in range(T):
    N = int(input())
    print(fibo_res[N][0], fibo_res[N][1])