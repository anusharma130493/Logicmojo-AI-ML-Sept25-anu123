d={'mobile1':10000, 'mobile2':11000, 'mobile3':13000, 'mobile4':9000, 'mobile5':15000, 'mobile6':16000, 'mobile7':17000, 'mobile8':18000, 'mobile9':19000}
print(d)
a = list(d.keys())
print("a " , a)
min_key = a[0]
min_value=d.get(min_key)
print("assume min ",min_value)
for key,values in (d.items()):
  if(values < min_value):
   min_key = key
   min_value=  values                                                   
print(min_key, ":" ,min_value)
