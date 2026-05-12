# 학번, 이름, 학과, 학년
class Student :
    def __init__(self, stu_no, stu_name, stu_dept, stu_grade=1):
        self.__stu_no = stu_no
        self.__stu_name = stu_name
        self.__stu_dept = stu_dept
        self.__stu_grade = stu_grade
    
    def set_stu_grade(self, stu_grade) :
        if 1 <= stu_grade <= 4 :
            self.__stu_grade = stu_grade
        else :
            print("1부터 4까지만 가능합니다")
    
    def get_stu_grade(self) :
        return self.__stu_grade
    
    def get_stu_no(self):
        return self.__stu_no

    def get_stu_name(self):
        return self.__stu_name

    def get_stu_dept(self):
        return self.__stu_dept