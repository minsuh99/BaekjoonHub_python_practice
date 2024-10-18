n = int(input())
shirt= [int(i) for i in input().split()]
t, p = map(int, input().split())

print(sum([(i//t)+1 if i%t != 0 else i//t for i in shirt]))
print(n//p, n%p)