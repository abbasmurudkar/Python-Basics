
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
elif(exp == "sqrt"):
    sqrt1 = num1 * num1
    sqrt2 = num2 * num2
    print("Square Root: ", sqrt1,sqrt2)
else:
    print("The expression is wrong")