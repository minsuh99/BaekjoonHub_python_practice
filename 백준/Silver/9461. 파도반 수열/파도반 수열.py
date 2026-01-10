T = int(input())
triangle = [0 for _ in range(101)]
triangle[1] = 1
triangle[2] = 1

for i in range(3, 101):
    triangle[i] = triangle[i - 2] + triangle[i - 3]

for _ in range(T):
    N = int(input())
    print(triangle[N])