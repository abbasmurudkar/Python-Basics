class name:
    def __init__(self,age,name):  #parent class
        self.age=age
        self.name=name
    def info(self):             #child inheriting from parents
        print("NAME:",self.name,"AGE:",self.age)

a=name(18,"ABBAS")
a.info()
