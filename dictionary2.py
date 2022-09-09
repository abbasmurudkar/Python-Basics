
def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1={'name':15,'age':18}
dict2={'pass':"PASS",'result':80}
print(Merge(dict1, dict2))
print(dict2)


