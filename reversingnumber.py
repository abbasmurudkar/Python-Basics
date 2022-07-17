number=int(input("ENTER NUMBER:"))

rever_se=0

while (number>0):
    remainder=number%10
    rever_se=(rever_se*10)+remainder
    number=number//10

print("The reverse number is:",rever_se)
