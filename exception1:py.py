a=5
b=0
list=[1,2,3,4];
try:
    print("SECOND ELEMENT = %d"%(list[1]))

    #this is will throw error
    print("FIFTH ELEMENT = %d" % (list[5]))
except:
    print("FIFTH ELEMENT IS NOT THERE")

else:
    print("Success")
try:
    c=a/b 
    print("NUMBER",c)
except ArithmeticError:
    print("0 can't be divide with number")
else:
    print("succes")
