def solution(clothes):
    from collections import defaultdict
    
    # 각 종류별 의상의 수를 세기 위한 딕셔너리
    clothes_count = defaultdict(int)
    
    # 각 종류별 의상 수 세기
    for item, kind in clothes:
        clothes_count[kind] += 1
    
    # 각 종류별 선택 가능 경우의 수 계산
    combinations = 1
    for count in clothes_count.values():
        combinations *= (count + 1)  # 의상을 입는 경우 + 입지 않는 경우
    
    # 아무것도 입지 않는 경우 1가지 제외
    return combinations - 1