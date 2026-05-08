a = int(input("첫번째 숫자 : "))
b = int(input("두번째 숫자 : "))

# a에 3, b에 5를 입력받았다고 가정하면
# 3 * 5 = 15 형태로 출력
# 1.
print(a,"*",b, "=",a*b)
# 2.
print('{0} * {1} = {2}' .format(a, b, a*b))
# 3.
print(f'{a} * {b} = {a*b}')
# console.log(`${a} * ${b} = ${a*b}`)
