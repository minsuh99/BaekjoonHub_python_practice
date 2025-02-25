n, m = map(int, input().split())

def backtrack(start, my_list):
    if len(my_list) == m:
        my_list = [str(j) for j in my_list]
        print(" ".join(my_list))
        return
    
    for i in range(n):
        if i + 1 not in my_list:
            my_list.append(i + 1)
            backtrack(start + 1, my_list)
            my_list.pop()
    
backtrack(0, [])