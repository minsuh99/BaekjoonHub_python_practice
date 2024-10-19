word = input().upper()

count_list = [word.count(chr(c)) for c in range(ord('A'), ord('Z')+1)]
max_count = count_list.count(max(count_list))
if max_count > 1:
    print("?")
elif max_count == 1:
    print(chr(ord('A') + count_list.index(max(count_list))))