# 3.학생 2명의 이름과 점수를 각각 입력받아 names 리스트와 scores 리스트에 순서대로 저장하고
# 저장된 리스트를 사용하여 grade라는 딕셔너리를 만드시오
# 조회하고 싶은 학생 이름을 입력받아, 
# 딕셔너리에 이름이 있으면 "OOO 학생의 점수는 XX점입니다."를 출력하고, 
# 없으면 "등록되지 않은 학생입니다."를 출력하시오.
names = []
scores = []

names.append(input("이름을 입력하세요 : "))
scores.append(input("점수를 입력하세요 : "))

names.append(input("이름을 입력하세요 : "))
scores.append(input("점수를 입력하세요 : "))

grade = {
    names[0] : scores[0],
    names[1] : scores[1]
}
name = input("검색할 학생 이름 : ")
if name in grade :
    print(f"{name} 학생의 점수는 {grade[name]}점입니다.")
else :
    print("등록되지 않은 학생입니다")