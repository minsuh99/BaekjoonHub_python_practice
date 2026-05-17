def solution(files):
    answer = []
    temp = []
    for file in files:
        head, number = "", ""
        number_idx = 0
        for i in range(len(file)):
            if file[i].isdigit():
                number_idx = i
                break
            head += file[i]
        
        for j in range(number_idx, min(len(file), number_idx + 5)):
            if not file[j].isdigit():
                break
            number += file[j]
        
        temp.append([head, number, file])
        
    temp.sort(key=lambda x:(x[0].lower(), int(x[1])))

    answer = [f[2] for f in temp]
        
        
            
    return answer