#Factorial number
def fact(n):
    f=1
    while n > 0:
        f = f * n
        n = n - 1
    return f
f = fact(5)
print(f)

#Prime number
def prime(n):
    flag = 0
    for i in range(2,n):
        if(n%2==0):
            flag=1
            break
    if flag == 0:
        print("Prime number")
    else:
        print("Not Prime Number")
p = prime(4)
print(p)