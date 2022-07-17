class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        area=2*3.14*self.radius*self.radius
        return area
    def circum(self):
        circume=2*3.14*self.radius
        return circume
num=eval(input("ENTER THE RADIUS"))
newcircle= circle(num)
print("AREA OF CIRCLE:",newcircle.area())
print("CIRCUMFERENCE OF CIRCLE:",newcircle.circum())



 
