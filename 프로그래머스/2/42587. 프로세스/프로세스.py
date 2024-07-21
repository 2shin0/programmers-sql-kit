from collections import deque

def solution(priorities, location):
    # 큐 초기화: (우선순위, 초기 위치) 튜플을 저장
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    execution_order = 0
    
    while queue:
        # 큐에서 프로세스를 하나 꺼냄
        current = queue.popleft()
        
        # 현재 프로세스보다 우선순위가 높은 프로세스가 큐에 있는지 확인
        if any(current[0] < item[0] for item in queue):
            queue.append(current)  # 우선순위가 높은 프로세스가 있다면 다시 큐에 넣음
        else:
            execution_order += 1  # 실행 순서 증가
            # 실행된 프로세스가 우리가 찾고자 하는 프로세스라면 순서 반환
            if current[1] == location:
                return execution_order