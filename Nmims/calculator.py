import math
num1 = float(input("Enter the first number: "))
exp = str(input("Enter the expression to be performed: "))
num2 = float(input("Enter the second number: "))
if(exp == "+"):
    add = num1 + num2
    print("Addition: ",add)
elif(exp == "-"):
    subtract = num1 - num2
    print("Substraction: ",subtract)
elif(exp == "*"):
    mul = num1 * num2
    print("Multiplication: ",mul)
elif(exp == "/"):
    div = num1 / num2
    print("Division: ", div)
elif(exp == "floor"):
    floor1 = math.floor(num1)
    floor2 = math.floor(num2)
    print("Floor: ",floor1,floor2)
elif(exp == "tan"):    #also we can use sin,tan,sqrt
    tan1 = math.tan(num1)
    tan2 = math.tan(num2)
    print("Tan ",tan1) 
elif(exp == "sqrt"):
    sqrt1 = math.sqrt(num1)
    sqrt2 = math.sqrt(num2)
    print("Square Root: ", sqrt1,sqrt2)
else:
    print("The expression is wrong")