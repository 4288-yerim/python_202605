# 학번, 이름, 학과, 학년
class Student :
    def __init__(self, stu_no, stu_name, stu_dept, stu_grade=1):
        self.__stu_no = stu_no
        self.__stu_name = stu_name
        self.__stu_dept = stu_dept
        self.__stu_grade = stu_grade
        
    # __stu_grade를 기준으로 get, set 메소드 만들기
    # grade의 값은 1부터 4까지만 허용, 그 외 값은
    # '1부터 4까지만 가능합니다' 출력 후 저장은 x
    # set_stu_grade, get_stu_grade
    
    def set_stu_grade(self, stu_grade) :
        if 1 <= stu_grade <= 4 :
            self.__stu_grade = stu_grade
        else :
            print("1부터 4까지만 가능합니다")
    
    def get_stu_grade(self) :
        return self.__stu_grade
    
    
hong = Student("1234", "홍길동", "컴퓨터")
# print(hong.get_stu_grade())
print(hong.__dict__)
print(hong.__stu_grade)

# hong.__stu_grade = 2
# print(hong.__stu_grade)