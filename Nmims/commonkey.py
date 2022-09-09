d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for keys, values in d1.items():
  for keys2 , values2 in d2.items():
    if(keys == keys2):
      d3[keys]=[values+values2]
print("COMMON VALUES:- ",d3)