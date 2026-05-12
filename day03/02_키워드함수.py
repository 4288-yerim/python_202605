## 파이썬의 함수는 자바의 오버로딩을 대체하는 방법으로
## 키워드 기반 파라미터를 사용한다.

# def java_sum2(x, y) :
#     print(f"합 : {x+y}")

def keyword_sum(x=0, y=0, z=0) :
    print(f"합 : {x+y+z}")
    
keyword_sum()
keyword_sum(1)
keyword_sum(1,2)
keyword_sum(1,2,3)
keyword_sum(1,z=100)
keyword_sum(y=10, z=20)
keyword_sum(z=20, y=10)
# 일반 인자값은 무조건 키워드 인자 앞에 존재
# keyword_sum(x=10, y=20, 30)