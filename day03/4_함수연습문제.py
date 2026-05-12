# # 1
# def reverse_func(*word) :
#     for a in word :
#         print(a[::-1], end=" ")

# reverse_func("java", "python", "html", "css")

# # 2
# def num_sum(*num, option = "even") :
#     odd_sum = 0
#     even_sum = 0
#     for a in num :
#         if a % 2 == 0 :
#             even_sum += a
#         else :
#             odd_sum += a
#     if option == "even" :
#         print(even_sum)
#     elif option == "odd" :
#         print(odd_sum)
#     else :
#         print("옵션 다시 확인하셈")
        

# num_sum(1,3,2,4,5,7,1) # 짝수의 합 출력
# num_sum(1,3,2,4,5,7,1, option="odd") # 홀수의 합 출력

# # 3.
# def num_pick(*number, option="max") :
#     if option == "max" :
#         print(max(number))
#     elif option == "min" :
#         print(min(number))
#     else :
#         print("옵션 확인점")

# num_pick(3,7,1,9,4,2,10,19) # 가장 큰 수 출력
# num_pick(3,7,1,9,4, option="min") # 가장 작은 수 출력

# 4
# def dedupe(*numbers) :
#     return list(set(numbers))
        
# num_list = dedupe(1,3,5,2,4,1,2,3) # 중복제거된 결과를 리턴
# print(num_list) # [1,3,5,2,4]

# # 5.
# def union_list(list1, list2, *list3) :
#     result = set(list1) | set(list2) | set(list3)
#     return list(result)
    
# list1 = [1,4,2,9,10,3]
# list2 = [3,5,9,2,8]

# union_list(list1, list2, 3,5,20,9,15,7)
# # 결과로 list1, list2, 숫자들(3,5,20,9,15,7)의
# # 중복없는 결과 리스트 리턴

# 6
# import random

# def ran_list(a, start=1, end=50) :
#     list = []
#     for i in range(a) :
#         n = random.randint(start,end)
#         list.append(n)
        
#     print(list)

# # 10부터 45숫자 중 6개 중복 없는 숫자 리스트 리턴
# ran_list(6, start=10, end=45)
# # 1부터 100숫자 중 5개 중복 없는 숫자 리스트 리턴
# ran_list(5, end=100)
# # 1부터 50숫자 중 10개 중복 없는 숫자 리스트 리턴
# ran_list(10)

# 7.
def str_num_sum(num) :
    sum = 0
    for a in str(num) :
        sum += int(a)
    return sum
        

print(str_num_sum(1352)) # 각 숫자를 한자리씩 구분한 후 더하기
                    # 11
print(str_num_sum(209479)) # 31