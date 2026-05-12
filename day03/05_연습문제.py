
human = {"홍길동" : 170, "김철수" : 185, "김영희" : 165}
# 딕셔너리에서 가장 큰 키를 찾아라

# human["홍길동"]
# human.get("홍길동")
name = max(human, key=human.get)
print(name)

# def a() :
#     print("a함수 호출")

# def b() :
#     print("b함수 호출")

# def c() :
#     print("c함수 호출")

# def d() : 
#     return "a"

# def test(func) :
#     func()


# test(a)
# test(c()) # => test(None)
# test(d()) # => test("a")