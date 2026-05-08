list = {}

while True : 
    c = input("1) 친구등록 2) 검색 3) 종료 : ")
    if c == '1' :
        name = input("name : ")
        phone = input("phone : ")
        list[name] = phone
    elif c == '2' :
        a = input("name : ")
        if a in list :
            print(list[a])
        else :
            print("not Found")
    elif c == '3' :
        break
    else :
        print("1~3사이의 숫자 입력하세요.")