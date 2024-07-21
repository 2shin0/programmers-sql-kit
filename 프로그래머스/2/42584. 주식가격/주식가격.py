def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 스택에 가격이 떨어지는 시점 처리
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    # 스택에 남아있는 인덱스들에 대해 남은 시간 처리
    while stack:
        idx = stack.pop()
        answer[idx] = n - idx - 1

    return answer