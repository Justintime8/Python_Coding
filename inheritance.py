class koreanfriedchickenclubmember:
    x = 0
    name = ""
    def __init__(self,nam):
      self.name = nam
      print(self.name,'I am constructed')

    def membership(self) :
        self.x = self.x + 1
        print(self.name,"We have", self.x)

class FootballFan(koreanfriedchickenclubmember) :
  points = 0
  def touchdown(self) :
    self.points = self.points + 7
    self.membership()
    print(self.name, "points", self.points)

s = koreanfriedchickenclubmember("Sherry")
s.membership()

j = FootballFan("Justin")
j.membership()
j.touchdown()
