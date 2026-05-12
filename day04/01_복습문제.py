#1.
def text_join(*txt, sep=" ") :
    print(sep.join(txt))
        
text_join("apple", "banana", "kiwi", "orange", sep="-")  
# apple-banana-kiwi-orange 출력
text_join("Python", "Java", "C++")  
# Python Java C++ 출력

#2.
def list_tool(numbers, mode="sort") :
    if mode == "reverse" :
        print(sorted(numbers, reverse=True))
    elif mode == "sum" :
        print(sum(numbers))
    else : 
        print(sorted(numbers))
    
list_tool([3, 1, 7, 2, 9])
# [1, 2, 3, 7, 9] 출력
list_tool([3, 1, 7, 2, 9], mode="reverse")  
# [9, 7, 2, 1, 3] 출력
list_tool([3, 1, 7, 2, 9], mode="sum")  
# 22 출력

#3.
def dict_pick(dic, option="max"):
    if option == "min":
        min_key = min(dic, key=dic.get)
        print({min_key: dic[min_key]})
    else:
        max_key = max(dic, key=dic.get)
        print({max_key: dic[max_key]})
        
dict_pick({"apple": 3, "banana": 5, "kiwi": 2})  
# {'banana': 5} 출력
dict_pick({"apple": 3, "banana": 5, "kiwi": 2}, option="min")  
# {'kiwi': 2} 출력

#4.


items = {"pen": 10, "note": 5}
inventory(items, "pen", 3)  
# {'pen': 13, 'note': 5} 출력
inventory(items, "note", -2)  
# {'pen': 10, 'note': 3} 출력
inventory(items, "colored pencil", 5)  
# {'pen': 10, 'note': 3, 'colored pencil' : 5} 출력