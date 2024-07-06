# n/2 개를 선택가능
# n/2 개 선택 중 종을 가장 다양하게 선택
# 그렇다면 n/2가 종의 수보다 크면 종의 수만큼 선택
# 아니라면 n/2가 종의 수보다 작다면 n/2를 출력

def solution(nums):
    answer = 0
    pocketmon = set(nums)
    
    if len(pocketmon) >= (len(nums)//2):
        answer = (len(nums)//2)
    else:
        answer = len(pocketmon)
    
    return answer

# def solution(nums):
#     answer = min(len(nums) // 2, len(set(nums)))
#     return answer