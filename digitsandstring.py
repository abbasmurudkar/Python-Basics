s= input("ENTER THE STRING")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("lenght of string:",l)
print("Digits in string:",d)
