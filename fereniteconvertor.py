class temperature:
    temp=0
    def __init__(self,temp):
        self.temp=temp
    def ferenite(self):
        result=float((9*self.temp)/5+32)
        return result
    def celcius(self):
        result=float((self.temp - 32)*5/9)
        return result

num=float(input("ENTER THE TEMPERATURE IN CELCIUS"))
t= temperature(num)
print(t.ferenite())

num=float(input("ENTER THE TEMPERATURE FOR CFERANITE"))
t=temperature(num)
print(t.celcius())
