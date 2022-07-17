
l1 = [13, 23, 25, 26, 30]
l2 = [19, 21, 23, 26, 40]
l3 = []

for i in range(len(l1)):
    l3.append(l2[i]*l1[i])
    print(l3)
print("MAXIMUM VALUE IN TUPLE: ", max(l1))
print("MINIMUM VALUE IN TUPLE: ", min(l2))

l3.reverse()
print(l3)

for i in l1:
    if i in l2:
        print("The Common Numbers:-", i)
for i in l1:
    if(i % 2 == 0):
        print("Even Numbers:-", i)