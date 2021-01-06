class koreanfriedchickenclubmember:
    x = 0
    name = ""
    def __init__(self,z):
      self.name = z
      print(self.name,'I am constructed')

    def membership(self) :
        self.x = self.x + 1
        print(self.name,"We have", self.x)

s = koreanfriedchickenclubmember("Sherry")
s.membership()

j = koreanfriedchickenclubmember("Justin")
j.membership()
s.membership()
