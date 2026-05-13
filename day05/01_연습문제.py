from student import Student

m = Math() # 'Math 클래스 객체를 생성했습니다.' 출력
print(m.math_sum(1,5,2,9,3,2,6)) # 모든 숫자의 합 출력
print(m.math_sum(1,5,2,9,3,2,6,8,7, option="odd")) # 홀수의 합 출력
print(m.math_sum(1,5,2,9,3,8, option="even")) # 짝수의 합 출력

print(m.math_max_min(1,5,2,9,3,2,6)) # 가장 큰 숫자 출력
print(m.math_max_min(1,5,2,9,3,2,6)) # 가장 작은 숫자 출력

s1 = Student("1234", "홍길동", 30, "인천") # 학번, 이름, 나이, 주소
s2 = Student("2341", "김철수", 25, "서울") 
s3 = Student("1234", "박영희", 28, "제주도")

print(f"{s1.get_stu_name()}의 학번은 {s1.get_stu_no()} 입니다.") # '홍길동의 학번은 1234 입니다' 출력
print(s1 == s2) # False
print(s1 == s3) # True (각 객체의 학번이 같으면 True가 나오도록)