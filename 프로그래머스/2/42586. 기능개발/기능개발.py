def solution(progresses, speeds):
    from math import ceil
    
    # 각 작업이 완료되기까지 필요한 일수 계산
    days_needed = [ceil((100 - prog) / speed) for prog, speed in zip(progresses, speeds)]
    
    # 배포 일정 관리
    result = []
    while days_needed:
        # 현재 배포할 작업의 기준 일수
        current_day = days_needed.pop(0)
        count = 1
        
        # 배포 가능한 작업들 묶기
        while days_needed and days_needed[0] <= current_day:
            days_needed.pop(0)
            count += 1
        
        result.append(count)
    
    return result