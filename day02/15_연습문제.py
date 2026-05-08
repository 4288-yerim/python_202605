# 학생관리 프로그램
# 동명이인 없다고 가정하고 실습
# 이름, 학과, 주소, 전화번호 입력받아서 저장
# 메뉴는 등록, 수정, 삭제, 검색, 종료

# 등록할때는 이미 등록된 이름일 경우 '이미 등록된 학생입니다' 출력
# 수정은 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 학과, 주소, 전화번호 다시 입력받아서 저장
# 삭제는 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 해당 학생 데이터 삭제
# 검색은 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 학생의 이름, 학과, 주소, 번호 출력 
# 종료는 프로그램 종료

student_list = {}
while True :
    print("=== 학생관리 프로그램 ===")
    print("메뉴를 선택해주세요.")
    menu = input("1) 등록 2) 수정 3) 삭제 4) 검색 5) 종료 : ")
    if menu == '1' :
        while True :
            name = input("등록할 이름을 입력해주세요 : ")
            if name in student_list :
                print("이미 등록된 학생입니다")
                print()
                continue
            dept = input("등록할 학과를 입력해주세요 : ")
            addr = input("등록할 주소를 입력해주세요 : ")
            phone = input("등록할 전화번호를 입력해주세요 : ")
            student_list[name] = [dept, addr, phone]
            print("등록되었습니다")
            print()
            break
    elif menu == '2' :
        re_name = input("수정할 학생의 이름을 입력해주세요 : ")
        if re_name in student_list :
            re_dept = input("등록할 학과를 입력해주세요 : ")
            re_addr = input("등록할 주소를 입력해주세요 : ")
            re_phone = input("등록할 전화번호를 입력해주세요 : ")
            student_list[re_name] = [re_dept, re_addr, re_phone]
            print("수정되었습니다")
            print()
        else :
            print("없는 학생입니다")
            print()
    elif menu == '3' :
        del_name = input("삭제할 학생의 이름을 입력해주세요 : ")    
        if del_name in student_list :
            student_list.pop(del_name)
            print("삭제되었습니다")
            print()
        else :
            print("없는 학생입니다")
            print()
    elif menu == '4' :
        get_name = input("검색할 학생의 이름을 입력해주세요 : ")
        if get_name in student_list :
            print()
            print(f"| 이름 : {get_name}")
            print(f"| 학과 : {student_list[get_name][0]}")
            print(f"| 주소 : {student_list[get_name][1]}'")
            print(f"| 전화번호 : {student_list[get_name][2]}")
            print()
        else :
            print("없는 학생입니다")
            print()
    elif menu == '5' :
        print("종료되었습니다")
        break
    else :
        print("1~5사이의 숫자만 입력해주세요")
        print()