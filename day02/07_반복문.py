# 입력한 숫자의 구구단을 출력
# ex) 3입력 시 3단 출력
# dan = int(input("단을 입력하세요 : "))

# for i in range(1,10) :
#     print(f"{dan} x {i} = {dan * i}")
    
# 2~9단까지 모두 출력
for x in range(2,10) : 
    print(f"=== {x}단 ===")
    for y in range(1,10) :
        print(f"{x} x {y} = {x * y}")
    print()
    
