import sys

# def sort_word(word1, word2):
#     if len(word2) < len(word1):
#         return word2, word1
#     elif len(word1) == len(word2):
#         if word2 < word1:
#             return word2, word1
#     return word1, word2 

N = int(sys.stdin.readline())
word_list = []

for _ in range(N):
    word_list.append(sys.stdin.readline().strip())

# for i in range(len(word_list)):
#     for j in range(i, len(word_list)):
#         word_list[i], word_list[j] = sort_word(word_list[i], word_list[j])
# 시간 초과 여기서 난듯

word_list = list(set(word_list)) # 중복 제거
word_list.sort() # 기준 2
word_list.sort(key=len) # 기준 1 / 이건 처음 알았다

for word in word_list:
    print(word)  