def solution(word):
    answer = 0
    found = False

    def dfs(cur_s):
        nonlocal answer, found

        if found:
            return
        
        if cur_s:
            answer += 1

        if cur_s == word:
            found = True
            return

        if len(cur_s) == 5:
            return

        for vowel in ["A", "E", "I", "O", "U"]:
            dfs(cur_s + vowel)

    dfs("")
    return answer