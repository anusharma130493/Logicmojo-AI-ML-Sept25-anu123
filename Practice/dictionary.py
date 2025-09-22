d= {'mobile':['Redmi', 'Samsung', 'Realme'], 'Laptop': ['Dell', 'HP'], 'TV': ['Videocon', 'Sony']}
print(d)
print(d.keys())
print(d.values())
print()
l= []
for keys,values in d.items():
  for val in values:
    l.append(keys +"_" +val)
print("list of values " ,l)