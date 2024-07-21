from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위의 트럭을 나타내는 큐
    bridge_weight = 0  # 현재 다리 위의 트럭들의 총 무게
    truck_weights = deque(truck_weights)  # 대기 중인 트럭들을 큐로 변환
    
    while bridge:
        time += 1
        # 가장 앞의 트럭이 다리를 건너면 다리에서 내리기
        bridge_weight -= bridge.popleft()
        
        if truck_weights:
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            if bridge_weight + truck_weights[0] <= weight:
                # 트럭이 다리에 오르면 다리 무게 업데이트
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                bridge_weight += new_truck
            else:
                # 트럭이 올라갈 수 없으면 다리에 빈 공간 추가
                bridge.append(0)
    
    return time