T = int(input())

for _ in range(T):
    stack = []
    temp = input().rstrip()
    res = "YES"
    
    for s in temp:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                res = "NO"
                break
    if stack:
        res = "NO"
    
    print(res)