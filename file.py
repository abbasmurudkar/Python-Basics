file = open("./python.txt","rt")
data = file.read()
words = data.split()
print("number of words in text file:",len(words))
