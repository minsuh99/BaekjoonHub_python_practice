import sys

while (nums := sys.stdin.readline()) != "0 0\n":
    a, b = map(int, nums.split())
    print(a+b)