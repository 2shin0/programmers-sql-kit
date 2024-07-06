def solution(phone_book):
    # 전화번호부 정렬
    phone_book.sort()
    
    # 인접한 번호끼리 접두어 관계가 있는지 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    return True