b=[]
a=[1,2,3,2,6,7,3]
for i in range(len(a)):
  if a[i] in b:
    continue
  b.append(a[i])
print(b)