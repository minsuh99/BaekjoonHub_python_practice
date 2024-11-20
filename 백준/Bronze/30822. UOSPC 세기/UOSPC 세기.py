n = int(input())
word = [i for i in input()]

check_list = [0] * 5
check_alphabet = ['u', 'o', 's', 'p', 'c']
for w in word:
    if w in check_alphabet:
        check_list[check_alphabet.index(w)] += 1

print(min(check_list))