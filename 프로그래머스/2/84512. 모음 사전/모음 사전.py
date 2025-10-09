import sys
sys.setrecursionlimit(10 ** 5)

answer = 0
flag = False

def solution(word):
    
    def backtrack(string, word):
        global answer
        global flag
        if string == word:
            flag = True
            
        if flag or len(string) == 5:
            return 

        for char in ["A", "E", "I", "O", "U"]:
            string += char
            answer += 1
            backtrack(string, word)
            if flag:
                break
            string = string[:-1]
    
    backtrack("", word)
    
    return answer