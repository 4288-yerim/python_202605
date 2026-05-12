# tv = Television(10, 15, True)
# tv.show() # 결과 : 10 15 True
# tv.setChannel(12) # 결과 : channel값이 12로 변경
# tv.getChannel() # 결과 : channel에 있는 값 리턴

class Television :
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def show(self) :
        print(self.channel, self.volume, self.on)
     
    def setChannel(self, channel) :
        self.channel = channel
    
    def getChannel(self) :
        return self.channel
    
tv = Television(10, 15, True)
tv.show()
tv.setChannel(12)
print(tv.getChannel())
tv.show()