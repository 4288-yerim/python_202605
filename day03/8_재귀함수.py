# 팩토리얼 (빠져나가는게 중요함)
# 5! => 5 * 4 * 3 * 2 * 1

def factor(x) : 
    if x == 1 : 
        return 1
    else : 
        return x * factor(x-1) 
# 5 * factor(x-1), 5 * 4 * factor(x-1) ...

print(factor(5))

