import sys
input = sys.stdin.readline

N, M = map(int, input().split())
word_list = dict()

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word not in word_list:
            word_list[word] = 1
        else:
            word_list[word] += 1

res_list = sorted(word_list, key = lambda x:(-word_list[x], -len(x), x))

for w in res_list:
    print(w)