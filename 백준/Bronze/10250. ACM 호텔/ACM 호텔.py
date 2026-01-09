import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room_number = N // H if N % H == 0 else N // H + 1
    floor = H if N % H == 0 else N % H
    print(f"{floor}{room_number:02d}")