#practical 15
class Employee:
    Name = ''
    Dept = ''
    sal = 0
    def __init__(self,N,D,S):
        self.Name = N
        self.Dept = D
        self.sal = S
        
    def disp(self):
        print("NAME: ", self.Name)
        print("Department: ", self.Dept)
        print("Slaray: ", self.sal)
obj = Employee("MOHD ABBAS MURUDKAR", "COMPUTER", 800000)
obj.disp()

# practical 15_1
class Student:
    Name = ""
    Rn = ""
    def get_Data(self,N,R):
        self.Name= N
        self.Rn = R
    def show_disp(self):
        print("Name = ", self.Name)
        print("Roll No = ", self.Rn)
class Result(Student):
    ptt1 = 0
    ptt2 = 0
    def get_d(self,p1,p2):
        self.ptt1 = p1
        self.ptt2 = p2
    def show_marks(self):
        print("The Marks For Ptt1 = ", self.ptt1)
        print("The Marks For Ptt2 = ", self.ptt2)
obj = Result()
obj.get_Data("ABBAS MURUDKAR",20)
obj.get_d(20,20)
obj.show_disp()
obj.show_marks()