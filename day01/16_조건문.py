age = int(input("나이 입력 : "))
price = 20000

# 1~6세미만 : 무료
if 1 <= age < 6 :
    print('무료입니다!')
# 6~60세미만 : price(20000)
elif 6 <= age < 60 :
    print(f'가격은 {price}원 입니다.')
elif 60 <= age < 130 :
    p = int(price * 0.5)
    print(f'가격은 {p}원 입니다.')
else : 
    print('나이를 다시 확인해주세요.')