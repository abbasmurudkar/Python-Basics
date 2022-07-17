print("WELCOME TO GYM STORE")
print("YOU WILL GET DISCOUNT IF YOU WILL BUY PRODUCT ABOVE 1000 QUANTITY")
name=str(input("ENTER THE NAME:"))
euip=str(input("ENTER THE PRODUCT NAME:"))
num1=eval(input("ENTER THE QUANTITY OF PRODUCT:"))
if(num1>=1000):
    num2=num1*100-100
    print("CONGRATULATION SIR YOU HAVE GOT 10% DISCOUNT FOR",num1,"PRODUCTS")
    print("YOUR NAME:",name)
    print("PRODUCT NAME:",euip)
    print("YOUR TOTAL AMOUNT:",num2)
    print("VISIT AGAIN")
else:
    num3=num1*100
    print("SIR YOUR PRODUCT QUANTITY IS NOT ABOVE 1000 QUANTITY")
    print("YOUR NAME:",name)
    print("PRODUCT NAME:",euip)
    print("TOTAL AMOUNT:",num3)
    print("VISIT AGAIN")

    
