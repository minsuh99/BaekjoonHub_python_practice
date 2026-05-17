from collections import defaultdict

def solution(genres, plays):
    answer = []

    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] += play
        genre_songs[genre].append((play, idx))
    
    # 장르를 총 재생 수 기준 내림차순 정렬
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)
    
    for genre in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        for play, idx in songs[:2]:
            answer.append(idx)
    
    return answer