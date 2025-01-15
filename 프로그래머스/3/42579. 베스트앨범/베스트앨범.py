def solution(genres, plays):
    answer = []
    genres_play_dict = {}
    
    for i, genre in enumerate(genres):
        if genre not in genres_play_dict:
            genres_play_dict[genre] = plays[i]
        else:
            genres_play_dict[genre] += plays[i]
    genres_play_dict = dict(sorted(genres_play_dict.items(), key = lambda x: -x[1])) 
    # 딕셔너리 정렬 검색,,
    
    for genre in list(genres_play_dict.keys()):
        idx_list = [g[0] for g in list(enumerate(genres)) if g[1] == genre]
        
        temp_plays = [play for play in list(enumerate(plays)) if play[0] in idx_list]
        temp_plays = sorted(temp_plays, key = lambda x: -x[1])
        final_idx = [i[0] for i in temp_plays[:2]]
        answer.extend(final_idx)
    return answer