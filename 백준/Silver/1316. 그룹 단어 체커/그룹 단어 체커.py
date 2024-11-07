T = int(input())
res = T
for _ in range(T):
    word = input()
    alphabet_list = sorted(list(set([a for a in word])))
    
    for alphabet in alphabet_list:
        sw = 0  
        if word.count(alphabet) > 1:
            bool_list = [1 if word[i] == alphabet else 0 for i in range(word.find(alphabet), len(word))]
            for i in range(1, len(bool_list)-1):
                if bool_list[i] - bool_list[i+1] == -1:
                    res -= 1
                    sw = 1
                    break
        if sw == 1: break
print(res)