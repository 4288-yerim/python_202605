# 사용자로부터 입력받은 문자열(영어, 대소문자 구문 x)에서
# 사용된 문자의 개수 딕셔너리 형태로 저장(공백은 제외)
# good luck => {"g" : 1, "o" : 2, "d" : 1 ....}

# text = input("문자열을 입력하세요 : ")

# result = {}

# for i in text.lower() :
#     if i == " ":
#         continue
    
#     if i in result :
#         result[i] += 1
#     else :
#         result[i] = 1
# print(result)

# ----------------------------------------------

txt = input("문자을 입력 : ")
word_dict = {}
# for word in txt :
#     if word in word_dict :
#         word_dict[word] += 1
#     else :
#         word_dict[word] = 1

# 대소문자 구분 없이 합쳐서 넣기
# 공백은 합쳐서 넣기
# for word in txt :
#     if word == " ":
#         continue
#     else :
#         word_dict[word.lower()] = word_dict.get(word.lower(), 0) + 1
        
# print(word_dict)

txt = txt.replace(" ", "").lower()
for word in txt :
    word_dict[word.lower()] = word_dict.get(word.lower(), 0) + 1

print(word_dict)

# 가장 많이 등장하는 문자와 해당 문자의 개수 출력
# key_ = max(word_dict, key = word_dict.get)
# print(f"{key_} : {word_dict[key_]}")          # 가장 많이 등장하는 문자가 두개라면 맨앞에 하나만 출력됨

max_value = max(word_dict.values())
# for k, v in word_dict.items() :
#     print(f"key : {k} value : {v}")

max_keys = []
for k in word_dict.keys() :
    if word_dict[k] == max_value :
        max_keys.append(k)

print(f"가장 많은 문자 : ", end = " ")
for v in max_keys :
    print(v, end = " ")
print(f"\n 개수 : {max_value}")
