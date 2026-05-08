# start = int(input("시작 숫자 : "))
# end = int(input("끝 숫자 : "))

# end보다 start 숫자가 더 크면 '끝 숫자가 더 큽니다.' 출력 후
# 두 숫자를 다시 입력 받을 수 있도록

sum = 0
while True :
    start = int(input("시작 숫자 : "))
    end = int(input("끝 숫자 : "))
    if start > end :
        print("시작 숫자가 더 큽니다. 다시 입력하세요.")
    else :
        break
    
for a in range(start, end+1) :
    sum += a
print(f"합 : {sum}")


while True :
    start = int(input("시작 숫자 : "))
    end = int(input("끝 숫자 : "))
    if start > end :
        print("시작 숫자가 더 큽니다. 다시 입력하세요.")
        continue
    sum = 0
    for a in range(start, end+1) :
        sum += a
    print(f"합 : {sum}")
    break