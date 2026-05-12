class Student :
    auto_increment = 0
    
    @classmethod
    def change_num(cls, num) :
        cls.auto_increment = num
    
    def __init__(self, name, dept):
        Student.auto_increment += 1
        self.__stu_no = Student.auto_increment
        self.__stu_name = name
        self.__stu_dept = dept
    def get_stu_no(self) : 
        return self.__stu_no
    
hong = Student("홍길동", "컴퓨터")
kim = Student("김철수", "기게")
park = Student("박영희", "디자인")

print(f"홍길동 학번 : {hong.get_stu_no()}")
print(f"김철수 학번 : {kim.get_stu_no()}")
print(f"박영희 학번 : {park.get_stu_no()}")

Student.auto_increment = 100
print(hong.__)