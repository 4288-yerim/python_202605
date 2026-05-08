list = [1,5,9,2,6]
# list.sort() # 오름차순
# list.sort(reverse=True) # 내림차순
# print(list)

# list.pop()
print("꺼낸 값 => ", list.pop()) # 맨 뒤에 값
print(list)
print("꺼낸 값 => ", list.pop(2)) # 2번째 인덱스
print(list)
print("꺼낸 값 => ", list.remove(5)) # 리턴 없음
print(list)

print(len(list))