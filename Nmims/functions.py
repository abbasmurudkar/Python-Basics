a = int(input("a:- "))
b = int(input("b:- "))
c = int(input("c:- "))
d = int(input("d:- "))
k = int(input("k:- "))
x = int(input("x:- "))
if(x>k):
    f = ((a*pow(x,3))-(b*pow(x,2))+(c*x)-d)
    print("f(x)= ",f)
elif(x==k):
    print("f(x)= 0")
else:
    f=((-a*pow(x,3))+(b*pow(x,2))-(c*x)+d)
    print("f(x)= ",f)
