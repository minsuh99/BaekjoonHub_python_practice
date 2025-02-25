n, m = map(int, input().split())
def backtrack(start, my_list):
    if len(my_list) == m:
        print(" ".join(map(str, my_list)))
        return
    
    for i in range(start, n):
        my_list.append(i + 1)
        backtrack(i + 1, my_list)
        my_list.pop()

backtrack(0, [])