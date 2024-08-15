import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * 1000001
    
    for i, operation in enumerate(operations):
        op, num = operation.split()
        num = int(num)
        
        if op == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        elif op == 'D':
            if num == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif num == -1:  # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]