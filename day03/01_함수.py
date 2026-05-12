# 함수 정의
def default_func() :
    print("파라미터 x, 리턴 x 함수")

# 2. 파라미터 있는 함수
def param_func(x) :
    print(f"전달 받은 값 : {x}")
    
# 3. 리턴이 있는 함수
def return_func(x,y) :
    return x+y

# 4. 리턴이 여러개인 함수
def return_func2(x,y) :
    return x+1, y-1

# 함수 호출
default_func()
param_func(10)
num = return_func(100, 200)
print(num)

a,b = return_func2(10, 10)
print(f"a : {a}, a : {b}")