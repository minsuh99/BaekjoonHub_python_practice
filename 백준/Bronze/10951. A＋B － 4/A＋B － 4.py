import sys

while (nums := sys.stdin.readline()) != "":
    a, b = map(int, nums.split())
    print(a+b)