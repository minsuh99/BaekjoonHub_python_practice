def solution(data, ext, val_ext, sort_by):
    cond_idx = ["code", "date", "maximum", "remain"].index(ext)
    sort_idx = ["code", "date", "maximum", "remain"].index(sort_by)
    
    data = sorted([[d[0], d[1], d[2], d[3]] for d in data if d[cond_idx] < val_ext], key=lambda x:x[sort_idx])
    
    return data