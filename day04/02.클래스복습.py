class Car :
    def __init__(self, speed, color, model):
        print("자동차 객체를 생성하였습니다.")
        self.speed = speed
        self.color = color
        self.model = model
    
    def getSpeed(self) :
        print(f"자동차의 속도는 {self.speed}")
    def setSpeed(self, speed) :
        self.speed = speed
    def getColor(self) :
        print(f"자동차의 색상은 {self.color}")
    def getModel(self) :
        print(f"자동차의 모델은 {self.model}")

car = Car(0, "blue", "E-class")
car.getSpeed()
car.getColor()
car.getModel()
car.setSpeed(60)
car.getSpeed()