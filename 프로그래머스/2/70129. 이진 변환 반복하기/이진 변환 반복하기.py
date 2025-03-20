def solution(s):
    answer = []
    ans1 = 0
    ans2 = 0
    temp = 0
    
    while s != "1":
        s_remove0 = "".join([i for i in s if i != '0'])
        temp = len(s_remove0)
        ans2 += (len(s) - temp)
        s = str(bin(temp))[2:]
        ans1 += 1
    answer = [ans1, ans2]


    return answer