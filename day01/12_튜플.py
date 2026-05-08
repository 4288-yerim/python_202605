# 파이썬의 리스트에는 이것저것 다 들어간다
tuple = [1, "홍길동", True, [2,3,4]]
print(tuple)
print(tuple[1]) # index 1번째
print(tuple[-1]) # index 뒤에서 0번째
print(tuple[1:]) # index 1부터 끝까지
# print(tuple[4]) # 에러(4번째 인덱스 없음)

# tuple[0] = 100 # 튜플은 수정 불가능
# print(tuple)