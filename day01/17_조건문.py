num_list = [1,3,5,6,10]
num = int(input('1~10 사이 숫자 입력 : '))

if num in num_list :
    print('성공!')
    if num % 2 == 0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")
else :
    print('실패!')

