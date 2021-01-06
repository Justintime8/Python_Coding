class koreanfriedchickenclubmember:
    x = 0

    def __init__(self):
      print('I am constructed')

    def membership(self) :
        self.x = self.x + 1
        print("We have", self.x)

    def __del__(self) :
      print('I am destructed', self.x)

member = koreanfriedchickenclubmember()
member.membership()
member.membership()
member = 8
print('member has', member)
