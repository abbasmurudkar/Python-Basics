
s1 = {20,30,40,50,60,70}
s2 = {40,30,20,10,30,40}
print("The Maximum Value", max(s1))
print("The Minimum Value", min(s1))
print("The length of sets: ", len(s1))

a  = s1.union(s2)
print(a)
x = s1.intersection(s2)
print(x)
y = s1.difference(s2)
print(y)
