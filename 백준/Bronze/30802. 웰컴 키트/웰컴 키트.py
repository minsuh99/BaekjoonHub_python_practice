N = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
T, P = map(int, input().split())

print(sum([i // T if i % T == 0 else i // T + 1 for i in [s, m, l, xl, xxl, xxxl]]))
print(N // P, N % P)