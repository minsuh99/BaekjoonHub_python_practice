def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        idx = 0
        flag = True
        for i in range(len(tree)):
            if tree[i] in skill:
                if tree[i] == skill[idx]:
                    idx += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1
    return answer