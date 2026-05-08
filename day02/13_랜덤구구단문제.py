import random

while True :
    ao = 0
    ax = 0
    q = int(input("풀고 싶은 문제 수를 입력하세요 (2~5) : "))
    if 2 <= q <= 5 :
        for i in range(0,q) :
            x = random.randint(2,9)
            y = random.randint(1,9)
            print()
            print(f"{i+1}번 문제 {x} x {y} = ?")
            a = int(input("정답 입력 : "))
            if a == (x*y) :
                print("정답입니다!")
                ao += 1
            else :
                print(f"틀렸습니다. 정답은 {x*y}입니다.")
                ax +=1
        print("-" * 30)
        print(f"결과 발표 : 맞춘 개수: {ao}, 틀린 개수: {ax}")
        print("-" * 30)
        yn = input("다시 하시겠습니까? (y/n) : ")
        if yn == 'y' :
            continue
        elif yn == 'n' :
            print("종료합니다.")
            break
    else :
        print("2 에서 5 사이의 숫자만 입력 가능합니다.")
        continue
    
# --------------------------------------------------------------------

# while True :
#     ao = 0
#     ax = 0
#     q = int(input("풀고 싶은 문제 수를 입력하세요 (2~5) : "))
#     if 2 <= q <= 5 :
#         for i in range(0,q) :
#             x = random.randint(2,9)
#             y = random.randint(1,9)
#             print()
#             print(f"{i+1}번 문제 {x} x {y} = ?")
#             a = int(input("정답 입력 : "))
#             if a == (x*y) :
#                 print("정답입니다!")
#                 ao += 1
#             else :
#                 print(f"틀렸습니다. 정답은 {x*y}입니다.")
#                 ax +=1
#         print("-" * 30)
#         print(f"결과 발표 : 맞춘 개수: {ao}, 틀린 개수: {ax}")
#         print("-" * 30)
#         while True :
#             yn = input("다시 하시겠습니까? (y/n) : ")
#             if yn == 'y' :
#                 break
#             elif yn == 'n' :
#                 print("종료합니다.")
#                 break
#             else :
#                 print("y 혹은 n을 입력하세요.")
#         if yn == 'n' :
#             break
#     else :
#         print("2 에서 5 사이의 숫자만 입력 가능합니다.")
#         continue

