def solution(arr):
    result = []
    prev = None
    
    for num in arr:
        if num != prev:
            result.append(num)
            prev = num
    
    return result