import random

# print(random.random())
# print(random.randint(1,10))

# fruits = ["사과", "오렌지", "바나나", "키위", "수박"]
# print(random.choice(fruits))

fruits = ["사과", "오렌지", "바나나", "키위", "수박"]
print(random.choice(fruits))
print(random.sample(fruits, 2))

print(f"셔플 전 => {fruits}")
print(random.choice(fruits))
print(f"셔플 후 => {fruits}")
