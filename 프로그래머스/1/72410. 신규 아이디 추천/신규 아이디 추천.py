def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    temp = ''
    for i in range(len(new_id)):
        if not new_id[i].isalpha() and not new_id[i].isdigit() and new_id[i] not in ["-", "_", "."]:
            pass
        else:
            temp += new_id[i]
    
    new_id = temp
    temp = ''

    for i in range(len(new_id)):
        if len(temp) > 0 and temp[-1] == new_id[i] == ".":
            pass
        else:
            temp += new_id[i]
    
    new_id = temp
    temp = ''
    
    new_id = new_id.lstrip(".").rstrip(".")
    
    if len(new_id) == 0:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.lstrip(".").rstrip(".")
        
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    
    answer = new_id
    print(new_id)
    return answer