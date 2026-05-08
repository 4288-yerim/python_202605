# 2. 과일 이름과 가격을 아래와 같이 딕셔너리로 저장한 후 
# 과일이름을 입력받아 해당 과일의 가격을 출력하시오.
# 단, 없는 과일을 입력하면 "판매하지 않는 상품입니다" 출력하시오.
fruit = {"사과": 1000, "바나나": 1500, "딸기": 2000}

name = input("과일 이름 입력 : ")
if name in fruit :
    print(f"{fruit[name]}원")
else :
    print("판매하지 않는 상품입니다")

# if name == '사과' :
#     print(fruit['사과'])
# elif name == '바나나' :
#     print(fruit['바나나'])
# elif name == '딸기' : 
#     print(fruit['딸기'])
# else :
#     print("판매하지 않는 상품입니다")