file = open("./python.txt","r")
counter=0

content=file.read()
colist=content.split("\n")

for i in colist:
    if i:
        counter +=1
print("THIS IS THE NUMBER OF LINES IN THE FIELD:")
print(counter)
