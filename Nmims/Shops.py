item= str(input("Enter the item name p-pants,s-shorts,t- shirts"))
amount = float(input("Enter the amount for item: "))
if(item == "p"):
    print("YOU HAVE SELECTED PANTS")
    if(amount <= 100):
        total= amount - 0.03
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 3%")
    if(amount >= 100 and amount<=200):
        total= amount - 0.08
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 8%")
    if(amount >= 200 and amount<=300):
        total= amount - 0.12
        print("TOTAL AMOUNT: ",total,"DISCOUNT OF 12%")
    
