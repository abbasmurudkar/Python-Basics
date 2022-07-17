x = "Hello I Am Abbas Murudkar"

low = 0
up = 0
for i in x:
    if i.isupper():
        up = up + 1
    elif i.islower():
        low = low + 1
    else:
        low = low
        up = up
print("NUMBER OF UPPERCASE: ", up)
print("NUMBER OF LOWERCASE: ",low)
print("COUNT OF A LETTER: ", x.count("A"))
print("REPLACING A LETTER WITH B ", x.replace("A","B"))