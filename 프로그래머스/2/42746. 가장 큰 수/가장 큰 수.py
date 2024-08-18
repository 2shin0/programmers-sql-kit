from functools import cmp_to_key

def compare(a, b):
    # 두 수를 이어 붙여서 비교
    if a + b > b + a:
        return -1  # a가 더 앞에 와야 함
    elif a + b < b + a:
        return 1  # b가 더 앞에 와야 함
    else:
        return 0  # 동일한 경우

def solution(numbers):
    # numbers의 각 요소를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 커스텀 정렬 기준을 사용하여 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 결과를 이어붙여서 출력
    answer = ''.join(numbers)
    
    # "0000" 같은 경우가 있을 수 있으므로 이 경우 "0"을 반환
    return answer if answer[0] != '0' else '0'