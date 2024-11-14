cnt_list = [0] * 26
word = input()

for w in word:
    cnt_list[ord(w) - ord('a')] += 1

for cnt in cnt_list:
    print(cnt, end=" ")