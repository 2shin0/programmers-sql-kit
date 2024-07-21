def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    # 완주하지 못한 선수를 찾는 부분
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    # 마지막 주자가 완주하지 못한 경우
    return participant[-1]