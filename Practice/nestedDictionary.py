l=[]
d={'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}
for keys,values in (d.items()):
  if(type(values) == dict):
    for key,value in (values.items()):
     l.append(keys+"_"+key + ":" + str(value))
  else:
    l.append(keys+":"+ str(values))
print(l) 