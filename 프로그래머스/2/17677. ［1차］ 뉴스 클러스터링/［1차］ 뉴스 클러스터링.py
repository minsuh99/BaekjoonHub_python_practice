from collections import Counter

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    arr1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    
    set1 = dict(Counter(arr1))
    set2 = dict(Counter(arr2))
    
    intersection = dict()
    union = dict()
    
    for key in set1.keys():
        if key in set2:
            intersection[key] = min(set1[key], set2[key])
            union[key] = max(set1[key], set2[key])

    while True:
        for key in set1.keys():
            union[key] = set1[key]
        
        for key in set2.keys():
            if key in intersection.keys():
                union[key] = max(set1[key], set2[key])
            else:
                union[key] = set2[key]
        
        break
    
    if sum(union.values()) == 0:
        answer = 65536
    else:
        answer = int(sum(intersection.values()) / sum(union.values()) * 65536)

    return answer