class Rect :
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __eq__(self, other) :
        return self.width * self.height == other.width * other.height

    def __gt__(self, other) :
        return self.width + self.height > other.width + other.height
    
r1 = Rect(4, 5)
r2 = Rect(2, 10)
print(r1 == r2) # wdith * height가 같다면 같은 객체로 판별 되
                # __eq__ 메소드 구현
print(r1 > r2)  # wdith + height가 더 크면 True 아니면 False