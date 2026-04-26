def solution(s):
    answer = []
    my_list = s[1:-1].split("},{")
    my_list = [c.replace("{", "").replace("}", "") for c in my_list]
    my_list = [set([int(i) for i in l.split(",")]) for l in my_list]
    my_list.sort(key=lambda x:len(x))
    
    for st in my_list:
        for element in st - set(answer):
            answer.append(element)
    return answer