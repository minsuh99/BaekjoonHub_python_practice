from collections import Counter


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    my_list1, my_list2 = [], []
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            my_list1.append(str1[i]+str1[i+1])
    
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            my_list2.append(str2[i]+str2[i+1])
    
    my_dict1, my_dict2 = Counter(my_list1), Counter(my_list2)
    all_keys = list(set(my_dict1.keys()) | set(my_dict2.keys()))
    if len(my_dict1) == 0 and len(my_dict2) == 0:
        return 65536
    
    inter_dict, union_dict = dict(), dict()
    for k in all_keys:
        if k in my_dict1 and k in my_dict2:
            inter_dict[k] = min(my_dict1[k], my_dict2[k])
        union_dict[k] = max(my_dict1.get(k, -1), my_dict2.get(k, -1))
    
    jaccard = int(sum(inter_dict.values()) / sum(union_dict.values()) * 65536)
    
    return jaccard