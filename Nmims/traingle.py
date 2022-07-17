print("ENTER THE THREE SIDES OF THE TIANGLE")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == b == c :
    print("EQUILATERAL TRAINGLE")
elif a==b or b == c or c == a:
    print("ISOCELES TRIANGLE")
else:
    print("SCALENE TRIANGLE")
