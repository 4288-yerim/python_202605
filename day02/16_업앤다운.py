import random

while True:
    num = random.randint(1, 100)
    count = 0
    print("==== 업다운 게임 ====")
    
    while True:
        print("1~100사이의 숫자를 입력해주세요")
        print("게임을 종료하려면 1001을 입력해주세요")
        answer = input("숫자 : ")

        if answer == '1001':
            print("종료되었습니다")
            exit()

        is_num = True
        for i in answer:
            if i < '0' or i > '9':
                print("| 숫자를 입력해주세요")
                print()
                is_num = False
                break
        if is_num == False:
            continue

        answer = int(answer)

        if answer < 1 or answer > 100:
            print()
            print("| 1~100사이의 숫자만 입력해주세요")
            print()
            continue
            

        if answer > num:
            print()
            print("▼ DOWN")
            print()
            count += 1

        elif answer < num:
            print()
            print("▲ UP")
            print()
            count += 1

        else:
            print()
            print(f"| 정답! {count}번만에 맞추셨습니다. |")
            print()

            retry = input("다시 하겠습니까? (y/n) : ").lower()

            if retry == 'y':
                break

            elif retry == 'n':
                print("게임 종료")
                exit()

            else:
                print("y/n을 입력해주세요")
                exit()