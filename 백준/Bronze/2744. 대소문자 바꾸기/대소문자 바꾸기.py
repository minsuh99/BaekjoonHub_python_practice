word = input()
word_list = []
for w in word:
    word_list.append(w.lower() if w.isupper() else w.upper())
print("".join(word_list))