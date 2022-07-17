from re import A


a = int(input("ENTER THE VALUE FOR A: "))
b = int(input("ENTER THE VALUE FOR B: "))
c = int(input("ENTER THE VALUE FOR C: "))
x1 = (-b + ((b**2 - 4*a*c)**0.5))/2*a
x2 = (-b - ((b**2 - 4*a*c)**0.5))/2*a
print("VALUE OF X:%.2f/%.2f" %(x1,x2))