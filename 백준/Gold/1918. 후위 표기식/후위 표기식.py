import sys
input = sys.stdin.readline

temp = input().rstrip()
stack = []
res = ""

for s in temp:
    if s.isalpha():
        res += s

    elif s == "(":
        stack.append(s)

    elif s == ")":
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.pop()

    else:
        while stack and stack[-1] != "(" and (stack[-1] in ["*", "/"] or (stack[-1] in ["+", "-"] and s in ["+", "-"])):
            res += stack.pop()
        stack.append(s)

while stack:
    res += stack.pop()

print(res)
