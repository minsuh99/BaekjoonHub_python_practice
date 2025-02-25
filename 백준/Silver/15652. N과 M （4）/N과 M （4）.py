n, m = map(int, input().split())
def backtrack(start, my_list):
    if len(my_list) == m:
        print(" ".join(map(str, my_list)))
        return
    
    for i in range(start, n):
        my_list.append(i + 1)
        backtrack(i, my_list) # 조합은 i + 1 이었음 근데 중복조합은 i도 뽑아도 되니까
        my_list.pop()

backtrack(0, [])