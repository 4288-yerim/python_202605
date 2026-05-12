class Human :
    def __init__(self, name, age):
        self.name = name
        self.age = age

hong = Human("홍길동", 30)
kim = Human("김철수", 25)
human = hong

hong.set_age(35)
print(kim.get_age()) # 25

human.set_age(32)
print(hong.get_age()) # 32

if hong is kim :
    print("hong이랑 kim이랑 같다") # 출력 x
if hong is human :
    print("hong이랑 human이랑 같다") # 출력 o
if human is not kim :
    print("human이랑 kim이랑 다르다") # 출력 x
    

def change_age(obj, age=1) :
    print(obj.get_name(), "님의 나이를 ", age , "증가시켰습니다.")
    obj.set_age(obj.get_age() + age)
    
yu = Human("유재석", 30)
park = Human("박명수", 25)
person = yu

change_age(yu, 3)
print(yu.get_age())