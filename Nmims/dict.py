dict={
    "1":"ABBAS",
    "2":"MUSKAN",
    "3":"MUSTAFA",
}
print(dict)
print("DICTIONARY VALUES:-",dict.values())
print("DICTIONARY KEYS:-", dict.keys())
d = {"5":"ANAS"}
dict["4"]="ARMAN"   #adding the dictionary 
dict.update(d)
print(dict)         #updating the dictionary
d2= dict.pop("3")   #Deleting the items from dictionary
print("REMOVED ITEM:-",d2)
d4 = dict.copy()    #Copy of the dictionary
print("COPIED DICTIONARY:-",d4)
d3 = len(dict)      #length of the dictionary
print("LENGTH OF DICTIONARY",d3)
d1 = dict.clear()   #clearing the dictionary
print(d1)