import sys
input = sys.stdin.readline

N = int(input())
temp = input().rstrip()
my_dict = {}
stack = []

for i in range(N):
    my_dict[chr(ord('A') + i)] = float(input())

for s in temp:
    if s.isalpha():
        stack.append(my_dict[s])
    elif s in ['+', '-', '*', '/']:
        num1 = stack.pop()
        num2 = stack.pop()
        if s == "+":
            stack.append(num2 + num1)
        elif s == "-":
            stack.append(num2 - num1)
        elif s == "*":
            stack.append(num2 * num1)
        elif s == "/":
            stack.append(num2 / num1)

print(f"{stack[0]:.2f}")