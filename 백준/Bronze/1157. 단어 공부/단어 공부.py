from collections import Counter
my_dict = Counter(input().upper())

max_used = max(my_dict.values())
check = [k for k in my_dict.keys() if my_dict[k] == max_used]

print("?" if len(check) > 1 else check[0])