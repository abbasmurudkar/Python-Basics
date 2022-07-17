# overriding 
class Area:
    def area(self,s):
        self.s = s
        return (self.s*self.s)
    def area(self,l,w):
        self.w= w
        self.l = l
        return (self.w * self.l)
obj = Area()
data = obj.area(4,12)
print(data)
data=obj.area(4)
print(data)

# overloading
class Overloading:
    def getdegree(self):
        print("I got degreee")
class undergroud:
    def getdegree(self):
        print("second")
class destructure:
    def getdegree(self):
        print("third")
d = Overloading()
d.getdegree()

a = undergroud()
a.getdegree()

c = destructure()
c.getdegree()