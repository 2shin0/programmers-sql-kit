def solution(genres, plays):
    from collections import defaultdict

    # 장르별 총 재생 횟수와 장르별 노래 리스트 초기화
    genre_play_count = defaultdict(int)
    genre_song_list = defaultdict(list)
    
    # 각 노래의 정보를 장르별로 저장
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        genre_song_list[genre].append((play, i))
    
    # 장르별 총 재생 횟수를 기준으로 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    # 각 장르별로 노래를 정렬하고 최대 두 개의 노래를 선택
    for genre, _ in sorted_genres:
        songs = sorted(genre_song_list[genre], key=lambda x: (-x[0], x[1]))
        result.extend([song[1] for song in songs[:2]])
    
    return result