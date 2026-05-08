# 1. 숫자를 3개 입력받아서 리스트에 저장한 후 평균을 출력하시오.
num_list = []
# a = int(input("첫번째 숫자 : "))
# num_list.append(a)
num_list.append(int(input("첫번째 숫자 : ")))
num_list.append(int(input("두번째 숫자 : ")))
num_list.append(int(input("세번째 숫자 : ")))

avg = sum(num_list) / len(num_list)
print(f"평균 : {avg}")

# sum_ = num_list[0] + num_list[1] + num_list[2]
# avg = sum_ / len(num_list)


