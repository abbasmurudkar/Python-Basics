def tables_(num,i):
    print(num,"X",i,"=",num*i)
    if(i<10):
        tables_(num , i+1)

num= int(input("Enter the table you want:"))
print("TABLE OF",num)
tables_(num, 1)


