A, B = map(str, input().split())

A, B = A[::-1], B[::-1]

print(A if A > B else B)