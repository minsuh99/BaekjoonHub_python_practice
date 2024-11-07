my_list = [chr(i) for i in range(ord('a'), ord('z')+1)]

word = input()

for alphabet in my_list:
    print(word.find(alphabet), end=" ")