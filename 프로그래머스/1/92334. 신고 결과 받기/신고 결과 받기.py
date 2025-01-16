def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    repo_num_dict = {}
    res_dict = {}
    
    for i in id_list:
        repo_num_dict[i] = 0
        res_dict[i] = 0
        
    for rep in list(set(report)):
        _, reported = map(str, rep.split())
        repo_num_dict[reported] += 1
    
    
    ban_list = [name[0] for name in repo_num_dict.items() if name[1] >= k]

    new_report = [repo.split() for repo in list(set(report))]
    
    for repo in new_report:
        if not ban_list:
            break
        else:
            if repo[1] in ban_list:
                answer[id_list.index(repo[0])] += 1
    return answer