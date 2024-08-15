def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # 배열의 i번째부터 j번째까지 자르고 정렬
        sliced_array = sorted(array[i-1:j])
        # 정렬된 배열에서 k번째 숫자를 answer에 추가
        answer.append(sliced_array[k-1])
    return answer