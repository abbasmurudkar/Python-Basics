class c1:
    def a(self):
        print("IN C1")
class c2(c1):
    def a(self):
        print("IN C2")
class c3(c1):
    def a(self):
        print("IN C3")
class c4(c2,c3):
    pass
obj=c4()
obj.a()
