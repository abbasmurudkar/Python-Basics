section1= set(["green","blue"])
section2 = set(["blue","yellow"])
print("ORIGINAL SETS:")
print(section1)
print(section2)
a=section1.symmetric_difference(section2)
print("\n Symmetric difference of section1 - section2:")
print(a)
b=section2.symmetric_difference(section1)
print("\n Symmetric difference of section2 - section1:")
print(b)
setsa = set([1,1,2,3,4,5])
setsb = set([1,5,6,7,8,9])
print("\n ORIGINAL SETS:")
print(setsa)
print(setsb)
a= setsa.symmetric_difference(setsb)
print("\n Symmetric difference of setsa - setsb")
print(a)
b= setsb.symmetric_difference(setsa)
print("\n Symmetric difference of setsb - setsa")
print(b)