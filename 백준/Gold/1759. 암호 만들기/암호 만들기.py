import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

L, C = map(int, input().split())
my_list = [i for i in input().rstrip().split()]
my_list.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in vowel]

vowel_cnt = 0
consonant_cnt = 0
visited = [False for _ in range(C)]


def backtrack(start, res_list):
    global vowel_cnt, consonant_cnt
    if len(res_list) == L:
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print("".join(res_list))
        return
    
    for i in range(start, C):
        if visited[i]:
            continue
        
        visited[i] = True
        if my_list[i] in vowel:
            vowel_cnt += 1
            res_list.append(my_list[i])
            backtrack(i + 1, res_list)
            res_list.pop()
            vowel_cnt -= 1
        
        elif my_list[i] in consonant:
            consonant_cnt += 1
            res_list.append(my_list[i])
            backtrack(i + 1, res_list)
            res_list.pop()
            consonant_cnt -= 1

        visited[i] = False

backtrack(0, [])