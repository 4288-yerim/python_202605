# 1. 문제 수 입력 받기(최소 2, 최대 5)
# 2. 랜덤 구구단 문제 출력
# 3. 맞춘개수, 틀린개수 출력
# 4. 다시 할지 말지 결정(y/n)

import random

while True:
    quiz_num = int(input("풀고 싶은 문제 수를 입력하세요 (2~5): "))
    if not (2 <= quiz_num <= 5):
        print("2에서 5 사이의 숫자만 입력 가능합니다.")
        continue

    correct_num = 0

    for i in range(1, quiz_num + 1):
        x = random.randint(2, 9)  # 2단 ~ 9단
        y = random.randint(1, 9)  # 1 ~ 9 곱하기
        
        print()
        print(f"[{i}번 문제] {x} x {y} = ?")
        
        
        answer = int(input("정답 입력: "))
        if answer == x * y:
            print("정답입니다!")
            correct_num += 1
        else:
            print(f"틀렸습니다. 정답은 {x * y}입니다.")

    print("-" * 30)
    print(f"결과 발표: 맞춘 개수: {correct_num}, 틀린 개수: {quiz_num-correct_num}")
    print("-" * 30)

    retry = input("다시 하시겠습니까? (y/n): ").lower()
    if retry != 'y':
        print("종료합니다.")
        break