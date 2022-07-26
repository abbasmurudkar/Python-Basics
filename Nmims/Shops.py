item= str(input("Enter the item name p-pants,s-shorts,t- shirts:-"))
amount = float(input("Enter the amount for item: "))
if(item == "p"):
    print("YOU HAVE SELECTED PANTS")
    if(amount <= 100):
        total= amount - amount / 100 * 3
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 3%")
    elif(amount >= 101 and amount<=200):
        total= amount - amount / 100 * 8
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 8%")
    elif(amount >= 201 and amount<=300):
        total= amount - amount / 100 * 12
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 12%")
    elif(amount>300):
        total = amount - amount / 100 * 20
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 20%")
    else:
        print("INVALID STATUS")
if(item == "s"):
    print("YOU HAVE SELECTED Shirts")
    if(amount <= 100):
        total= amount
        print("TOTAL AMOUNT: ",total)
    elif(amount >= 101 and amount<=200):
        total= amount - amount / 100 * 5
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 5%")
    elif(amount >= 201 and amount<=300):
        total= amount - amount / 100 * 10
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 10%")
    elif(amount>300):
        total = amount - amount / 100 * 18
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 18%")
    else:
        print("INVALID STATUS")
if(item == "t"):
    print("YOU HAVE SELECTED T-shirts")
    if(amount <= 100):
        total= amount - amount / 100 * 5
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 5%")
    elif(amount >= 101 and amount<=200):
        total= amount - amount / 100 * 10
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 10%")
    elif(amount >= 201 and amount<=300):
        total= amount - amount / 100 * 15
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 15%")
    elif(amount>300):
        total = amount - amount / 100 * 22
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 22%")
    else:
        print("INVALID STATUS")
